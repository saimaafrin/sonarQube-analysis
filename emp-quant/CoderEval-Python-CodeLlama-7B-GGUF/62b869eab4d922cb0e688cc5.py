def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
	"""
	Together with :func:``update_last_applied_manifest_list_from_resp``, this
function is called recursively to update a partial ``last_applied_manifest``
from a partial Kubernetes response

Args:
    last_applied_manifest (dict): partial ``last_applied_manifest`` being
        updated
    observer_schema (dict): partial ``observer_schema``
    response (dict): partial response from the Kubernetes API.

Raises:
    KeyError: If the observed field is not present in the Kubernetes response

This function go through all observed fields, and initialized their value in
last_applied_manifest if they are not yet present
	"""
	for field in observer_schema["observed_fields"]:
		if field not in last_applied_manifest:
			last_applied_manifest[field] = {}
		if "observed_fields" in observer_schema:
			for sub_field in observer_schema["observed_fields"]:
				if sub_field not in last_applied_manifest[field]:
					last_applied_manifest[field][sub_field] = {}
				if "observed_fields" in observer_schema["observed_fields"][sub_field]:
					update_last_applied_manifest_dict_from_resp(
						last_applied_manifest[field][sub_field],
						observer_schema["observed_fields"][sub_field],
						response[field][sub_field],
					)
				else:
					last_applied_manifest[field][sub_field] = response[field][sub_field]
		else:
			last_applied_manifest[field] = response[field]