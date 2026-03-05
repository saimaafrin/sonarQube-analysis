def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    for key, value in observer_schema.items():
        if key in response:
            if isinstance(value, dict):
                if key not in last_applied_manifest:
                    last_applied_manifest[key] = {}
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest[key], value, response[key]
                )
            else:
                last_applied_manifest[key] = response[key]
        else:
            raise KeyError(f"Observed field '{key}' not present in the Kubernetes response")