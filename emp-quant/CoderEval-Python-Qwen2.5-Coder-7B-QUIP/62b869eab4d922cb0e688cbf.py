def generate_default_observer_schema(app):
    """
    Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
    """
    default_schema = {
        "apiVersion": "v1",
        "kind": "Pod",
        "spec": {
            "containers": [
                {
                    "name": "default-container",
                    "image": "default-image",
                    "resources": {
                        "requests": {
                            "cpu": "500m",
                            "memory": "512Mi"
                        },
                        "limits": {
                            "cpu": "1000m",
                            "memory": "1024Mi"
                        }
                    }
                }
            ]
        }
    }
    return default_schema