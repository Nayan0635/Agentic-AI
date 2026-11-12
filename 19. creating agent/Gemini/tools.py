import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions import *

tools = [
    {
        "function_declarations": [
            {
                "name": "addNumbers",
                "description": addNumbers.__doc__,
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            },
            
            {
                "name": "addNumbers",
                "description": multiplyNumbers.__doc__,
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            },

            {
                "name": "saveFile",
                "description": saveFile.__doc__,
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "content": {
                            "type": "STRING"
                        }
                    },
                    "required": ["content"]
                }
            },

            {
                "name": "readFile",
                "description": readFile.__doc__,
                "parameters": {
                    "type": "OBJECT",
                    "properties": {}
                }
            }
        ]
    }
]
