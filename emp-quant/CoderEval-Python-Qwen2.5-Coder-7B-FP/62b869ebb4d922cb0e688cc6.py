def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
# Iterate over each field in the observer schema
	for field in observer_schema:
		# Check if the current field is a dictionary
		if isinstance(field, dict):
			# Initialize an empty list for the current field in the
			# last_applied_manifest
			last_applied_manifest.append([])
			# Recursively call the function to update the nested
			# last_applied_manifest
			update_last_applied_manifest_list_from_resp(
				last_applied_manifest[-1], field["schema"], response
			)
		else:
			# If the current field is not a dictionary, check if it exists in
			# the response
			if field in response:
				# If the field exists in the response, add its value to the
				# last_applied_manifest
				last_applied_manifest.append(response[field])
			else:
				# If the field does not exist in the response, initialize its
				# value as None in the last_applied_manifest
				last_applied_manifest.append(None)