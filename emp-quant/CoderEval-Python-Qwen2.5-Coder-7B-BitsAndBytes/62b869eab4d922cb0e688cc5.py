for key, value in observer_schema.items():
    if isinstance(value, dict):
        if key not in last_applied_manifest:
            last_applied_manifest[key] = {}
        update_last_applied_manifest_dict_from_resp(last_applied_manifest[key], value, response.get(key, {}))
    else:
        if key not in last_applied_manifest:
            last_applied_manifest[key] = response.get(key)