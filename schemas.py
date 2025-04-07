tool_schemas = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Fetch current weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search internal documents using a query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                },
                "required": ["query"]
            }
        }
    }
]