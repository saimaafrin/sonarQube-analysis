def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for resource in app.spec.manifest:
		if resource.kind not in app.spec.observer_schema:
			app.spec.observer_schema[resource.kind] = {
				"kind": resource.kind,
				"spec": {
					"$ref": "#/definitions/io.k8s.api." + resource.kind.lower() + ".v1.PodSpec"
				},
				"status": {
					"$ref": "#/definitions/io.k8s.api." + resource.kind.lower() + ".v1.PodStatus"
				}
			}