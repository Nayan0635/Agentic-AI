from functions import *

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'addNew',
            'description': addNew.__doc__,
            'parameters': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'address': {'type': 'string'},
                    'course': {'type': 'string'}
                },
                'required': [
                    'name',
                    'email',
                    'address',
                    'course'
                ]
            }
        }
    },
# tool
    {
        'type': 'function',
        'function': {
            'name': 'showALL',
            'description': showALL.__doc__,
            'parameters': {
                'type': 'object',
                'properties': {}
            }
        }
    }
]