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