import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions import *

# openai specific tool calling
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'showAll',
            'description': showAll.__doc__,
            'parameters': {}
        }
    },
    
    {
        'type': 'function',
        'function': {
            'name': 'addNew',
            'description': addNew.__doc__,
            'parameters': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'}
                },
                'required': ['name', 'email']
            }
        }
    },
    
    {
        'type': 'function',
        'function': {
            'name': 'update',
            'description': update.__doc__,
            'parameters': {
                'type': 'object',
                'properties': {
                    'id' : {'type' : 'integer'},
                    'name': {'type': 'string'},
                    'email': {'type': 'string'}
                },
                'required': ['id', 'name', 'email']
            },
        }
    }, 
    
    {
        'type': 'function',
        'function': {
            'name': 'delete',
            'description': delete.__doc__,
            'parameters': {
                'type' : 'object',
                'properties': {
                    'id' : {'type' : 'integer'},
                },
                'required': ['id']
            },
        }
    }
]