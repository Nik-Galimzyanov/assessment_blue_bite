create_objects_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "batch_id": {
            "type": "string"
        },
        "objects": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "object_id": {
                            "type": "string"
                        },
                        "data": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": [
                                                "string",
                                                "number",
                                                "boolean",
                                                "null"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "key",
                                        "value"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "object_id",
                        "data"
                    ]
                }
            ]
        }
    },
    "required": [
        "batch_id",
        "objects"
    ]
}

get_objects_by_params_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string"
                },
                "value": {
                    "type": [
                        "string",
                        "number",
                        "boolean",
                        "null"
                    ]
                }
            },
        }
    ]
}