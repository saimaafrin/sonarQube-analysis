def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
# Iterate over each key-value pair in the observer schema
	for key, value in observer_schema.items():
		if isinstance(value, dict):
			# Recursively call the function for nested dictionaries
			update_last_applied_manifest_dict_from_resp(
				last_applied_manifest.get(key, {}), value, response.get(key, {})
			)
		else:
			# Check if the key exists in the response
			if key not in response:
				# Raise an error if the key is missing
				raise KeyError(f"Observed field '{key}' not found in Kubernetes response")
			# Update the last_applied_manifest dictionary with the value from the response
			last_applied_manifest[key] = response[key]