
import iso8601

from firegorest import tidy_doc


orig_data = {
    'approved_at': {'nullValue': None},
    'bank_id': {'stringValue': 'HDBCVNVX'},
    'created_at': {'timestampValue': '2019-12-15T03:42:30.691Z'},
    'loan_amount': {'integerValue': '200000000'},
    'isEmployee': {'booleanValue': False},
    'clients': {
        'arrayValue': {
            'values': [{'stringValue': 'web_s_housing_dev'}, {'stringValue': 'web_s_housing_prod'}]
        }
    },
    'loan_status': {
        'mapValue': {
            'fields': {
                'message': {'nullValue': None},
                'status': {'stringValue': 'draft'}
            }
        }
    },
}

neat_data = {
    'approved_at': None,
    'bank_id': 'HDBCVNVX',
    'created_at': iso8601.parse_date('2019-12-15T03:42:30.691Z'),
    'loan_amount': 200000000,
    'isEmployee': False,
    'clients': ['web_s_housing_dev', 'web_s_housing_prod'],
    'loan_status': {
        'message': None,
        'status': 'draft'
    }
}


def test_convert():
    assert tidy_doc(orig_data) == neat_data
