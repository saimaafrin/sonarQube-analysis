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
                    "ready": {
                        "type": "boolean"
                    }
                },
                "required": ["phase", "ready"]
            }
        },
        "required": ["status"]
    }
    return default_schema