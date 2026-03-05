import json

def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
    """
    default_schema = {
        "type": "object",
        "properties": {},
        "required": []
    }

    for resource in app.spec.manifest:
        if 'observer' not in resource or not resource['observer']:
            resource_name = resource['kind']
            resource_schema = {
                "type": "object",
                "properties": {
                    "metadata": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "namespace": {"type": "string"}
                        },
                        "required": ["name"]
                    },
                    "status": {
                        "type": "object",
                        "properties": {}
                    }
                },
                "required": ["metadata"]
            }
            default_schema['properties'][resource_name] = resource_schema

    return default_schema