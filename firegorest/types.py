# Utility to reduce data returned in Firestore trigger event

from datetime import datetime
from typing import Dict, Union, List

# Ref: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Value

# Primitive data types us
# kyed in Firestore REST document
FirePrim = Union[None, bool, float, str]
PrimitifType = Union[None, bool, int, float, str, bytes, datetime]
SimpleType = Union[PrimitifType, List[PrimitifType], Dict[str, PrimitifType]]


class GCFContext:
    '''Just a fake type, to help auto-completion in IDE.
    The real type is 'google.cloud.functions_v1.context.Context', which only exists
    when the function is run inside Google Cloud Function runtime.
    '''
    # Ex: 83006d7a-af1b-4833-8bc4-ab4ac8a374f9-0
    event_id: str
    # Ex: 2019-12-14T10:18:29.911055Z
    timestamp: str
    # Ex: providers/cloud.firestore/eventTypes/document.write
    event_type: str
    # Ex: projects/sunshine-super-app/databases/(default)/documents/customers/m7t5AzdqttyuRaZB4fHX
    resource: str
