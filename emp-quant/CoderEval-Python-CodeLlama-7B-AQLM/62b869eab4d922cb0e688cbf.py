def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for resource in app.spec.manifest:
		if resource.kind not in app.spec.observer_schema:
			app.spec.observer_schema[resource.kind] = {
				"type": "object",
				"properties": {
					"metadata": {
						"type": "object",
						"properties": {
							"name": {
								"type": "string"
							},
							"namespace": {
								"type": "string"
							},
							"labels": {
								"type": "object"
							},
							"annotations": {
								"type": "object"
							}
						}
					},
					"spec": {
						"type": "object",
						"properties": {
							"replicas": {
								"type": "integer"
							},
							"template": {
								"type": "object",
								"properties": {
									"metadata": {
										"type": "object",
										"properties": {
											"labels": {
												"type": "object"
											},
											"annotations": {
												"type": "object"