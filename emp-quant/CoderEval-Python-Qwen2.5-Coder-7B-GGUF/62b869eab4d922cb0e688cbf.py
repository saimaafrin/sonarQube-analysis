def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
    """
    default_schema = {
        "type": "object",
        "properties": {
            "status": {
                "type": "object",
                "properties": {
                    "phase": {
                        "type": "string"
                    },
                    "conditions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string"
                                },
                                "status": {
                                    "type": "string"
                                },
                                "lastTransitionTime": {
                                    "type": "string"
                                }
                            },
                            "required": ["type", "status", "lastTransitionTime"]
                        }
                    }
                }
            }
        }
    }
    return default_schema