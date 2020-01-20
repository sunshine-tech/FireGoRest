from typing import Dict, List, Any

import iso8601

from .types import FirePrim, SimpleType

_NAIVE_TYPE_MAP = {
    'nullValue': None,   # Original value is already None, no need to convert
    'stringValue': None,  # Original value is already str, no need to convert
    'doubleValue': None,  # Original value is already float
    'booleanValue': None,  # Orinial value is already bool
    'timestampValue': iso8601.parse_date,
    'integerValue': int,   # Original value is a string
    'bytesValue': bytes,  # Original value is a string
}


def naive_convert_field_value(desc: Dict[str, FirePrim]) -> SimpleType:
    data_type, value = next(iter(desc.items()))
    func = _NAIVE_TYPE_MAP[data_type]
    if func is None:
        return value
    return func(value)


def convert_field_value(desc: Dict[str, Any]) -> SimpleType:
    if 'mapValue' in desc:
        try:
            value_map = desc['mapValue']['fields']
        except KeyError:
            return {}
        return {k: convert_field_value(v) for k, v in value_map.items()}
    if 'arrayValue' in desc:
        try:
            value_array = desc['arrayValue']['values']   # type: List[Dict[str, FirePrim]]
        except KeyError:
            return []
        return [convert_field_value(v) for v in value_array]
    return naive_convert_field_value(desc)


def tidy_doc(firedoc: Dict[str, Any]) -> Dict[str, SimpleType]:
    ''' Convert a verbose Firestore REST Document data to a neat dict '''
    return {k: convert_field_value(v) for k, v in firedoc.items()}
