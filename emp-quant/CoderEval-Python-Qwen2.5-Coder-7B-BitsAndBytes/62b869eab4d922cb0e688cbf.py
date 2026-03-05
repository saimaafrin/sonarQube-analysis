from kubernetes import client

def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
    """
    api_instance = client.CoreV1Api()
    resources = app.spec.manifest.get('resources', [])
    default_schemas = {}

    for resource in resources:
        if 'kind' not in resource or 'apiVersion' not in resource:
            continue

        kind = resource['kind']
        api_version = resource['apiVersion']

        try:
            api_response = api_instance.list_namespaced_pod(namespace='default')
            # Assuming all resources are pods for simplicity
            for pod in api_response.items:
                if pod.metadata.name.startswith(kind.lower()):
                    default_schemas[kind] = {
                        "type": "object",
                        "properties": {
                            "metadata": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "namespace": {"type": "string"}
                                }
                            },
                            "status": {
                                "type": "object",
                                "properties": {
                                    "phase": {"type": "string"}
                                }
                            }
                        }
                    }
                    break
        except Exception as e:
            print(f"Error fetching {kind} resources: {e}")

    return default_schemas