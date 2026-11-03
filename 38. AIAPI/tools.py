from crud import *
tools =[
    {
        "type":"function",
        "function":{
            "name":"addNewPost",
            "description":addNewPost.__doc__,
            "parameters":{
                "type":"object",
                "properties":{
                    "title":{"type":"string"},
                    "desc":{"type":"string"}
                },
                "required":['title','desc']
            }
        }
    },
    {
            "type":"function",
            "function":{
                "name":"getAllPosts",
                "description":getAllPosts.__doc__,
                "parameters":{
                    "type":"object",
                    "properties":{}
                }
            }
    },
    {
        "type": "function",
        "function": {
            "name": "getPost",
            "description": getPost.__doc__,
            "parameters": {
                "type": "object",
                "properties": {
                    "post_id": {"type": "integer"}
                },
                "required": ["post_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "updatePost",
            "description": updatePost.__doc__,
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "desc": {"type": "string"},
                    "post_id": {"type": "integer"}
                },
                "required": ["title", "desc", "post_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "deletePost",
            "description": deletePost.__doc__,
            "parameters": {
                "type": "object",
                "properties": {
                    "post_id": {"type": "integer"}
                },
                "required": ["post_id"]
            }
        }
    }

]