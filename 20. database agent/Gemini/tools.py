import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions import *

tools = [
    {
        'name': 'showAll',
        'description': showAll.__doc__,
        'parameters': {
            'type': 'OBJECT',
            'properties': {}
        }
    },
    {
        'name': 'addNew',
        'description': addNew.__doc__,
        'parameters': {
            'type': 'OBJECT',
            'properties': {
                'name': {'type': 'STRING'},
                'email': {'type': 'STRING'}
            },
            'required': ['name', 'email']
        }
    },
    {
        'name': 'update',
        'description': update.__doc__,
        'parameters': {
            'type': 'OBJECT',
            'properties': {
                'id': {'type': 'INTEGER'},
                'name': {'type': 'STRING'},
                'email': {'type': 'STRING'}
            },
            'required': ['id', 'name', 'email']
        }
    },
    {
        'name': 'delete',
        'description': delete.__doc__,
        'parameters': {
            'type': 'OBJECT',
            'properties': {
                'id': {'type': 'INTEGER'}
            },
            'required': ['id']
        }
    }
]