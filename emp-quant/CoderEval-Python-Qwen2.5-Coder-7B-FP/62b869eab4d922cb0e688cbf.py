def generate_default_observer_schema(app):
observer_schemas = {}
	for resource_name, resource_spec in app.spec.manifest.items():
		if 'kind' not in resource_spec:
			continue
		resource_kind = resource_spec['kind']
		default_observer_schema = {
			"properties": {},
			"type": "object"
		}
		for field_name, field_spec in resource_spec.get('spec', {}).items():
			field_type = field_spec.get('type')
			if field_type == 'string':
				default_observer_schema['properties'][field_name] = {"type": "string"}
			elif field_type == 'integer':
				default_observer_schema['properties'][field_name] = {"type": "number", "format": "int64"}
			elif field_type == 'boolean':
				default_observer_schema['properties'][field_name] = {"type": "boolean"}
			elif field_type == 'array':
				array_items = field_spec.get('items', {})
				items_type = array_items.get('type')
				if items_type == 'string':
					default_observer_schema['properties'][field_name] = {"type": "array", "items": {"type": "string"}}
				elif items_type == 'integer':
					default_observer_schema['properties'][field_name] = {"type": "array", "items": {"type": "number", "format": "int64"}}
				elif items_type == 'boolean':
					default_observer_schema['properties'][field_name] = {"type": "array", "items": {"type": "boolean"}}
			else:
				default_observer_schema['properties'][field_name] = {"type": "object"}
		observer_schemas[resource_name] = default_observer_schema
	return observer_schemas