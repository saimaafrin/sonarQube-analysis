def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
	"""
	Together with :func:``update_last_applied_manifest_dict_from_resp``, this
function is called recursively to update a partial ``last_applied_manifest``
from a partial Kubernetes response

Args:
    last_applied_manifest (list): partial ``last_applied_manifest`` being
        updated
    observer_schema (list): partial ``observer_schema``
    response (list): partial response from the Kubernetes API.

This function go through all observed fields, and initialized their value in
last_applied_manifest if they are not yet present
	"""
	for field in observer_schema:
		if field["type"] == "object":
			if field["name"] not in last_applied_manifest:
				last_applied_manifest[field["name"]] = {}
			update_last_applied_manifest_dict_from_resp(
				last_applied_manifest[field["name"]],
				field["fields"],
				response[field["name"]],
			)
		elif field["type"] == "list":
			if field["name"] not in last_applied_manifest:
				last_applied_manifest[field["name"]] = []
			for i in range(len(response[field["name"]])):
				if i >= len(last_applied_manifest[field["name"]]):
					last_applied_manifest[field["name"]].append({})
				update_last_applied_manifest_list_from_resp(
					last_applied_manifest[field["name"]][i],
					field["fields"],
					response[field["name"]][i],
				)
		else:
			if field["name"] not in last_applied_manifest:
				last_applied_manifest[field["name"]] = response[field["name"]]