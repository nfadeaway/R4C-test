import jsonschema
from jsonschema import validate


def validate_robot_JSON_data(jsondata):
    schema = {
        'type': 'object',
        'properties': {
            'model': {
                'type': 'string',
                'minLength': 2,
                'maxLength': 2,
            },
            'version': {
                'type': 'string',
                'minLength': 2,
                'maxLength': 2,
            },
            'created': {
                'type': 'string',
                'pattern': '^((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])\s([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
            }
        },
        'required': ['model', 'version', 'created']
    }
    try:
        validate(jsondata, schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
