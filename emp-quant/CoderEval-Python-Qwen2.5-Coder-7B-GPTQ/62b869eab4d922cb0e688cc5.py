for key, value in observer_schema.items():
    if isinstance(value, dict):
        if key not in last_applied_manifest:
            last_applied_manifest[key] = {}
        update_last_applied_manifest_dict_from_resp(last_applied_manifest[key], value, response.get(key, {}))
    elif isinstance(value, list):
        if key not in last_applied_manifest:
            last_applied_manifest[key] = []
        for item in value:
            if isinstance(item, dict):
                last_applied_manifest[key].append({})
                update_last_applied_manifest_dict_from_resp(last_applied_manifest[key][-1], item, response.get(key, [{}])[0])
            else:
                last_applied_manifest[key].append(response.get(key, [item])[0])
    else:
        if key not in last_applied_manifest:
            last_applied_manifest[key] = response.get(key)