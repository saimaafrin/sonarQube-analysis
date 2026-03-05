for key, value in observer_schema.items():
    if key not in last_applied_manifest:
        if isinstance(value, dict):
            last_applied_manifest[key] = {}
            update_last_applied_manifest_dict_from_resp(last_applied_manifest[key], value, response.get(key, {}))
        elif isinstance(value, list):
            last_applied_manifest[key] = []
            update_last_applied_manifest_list_from_resp(last_applied_manifest[key], value, response.get(key, []))
        else:
            last_applied_manifest[key] = response.get(key)