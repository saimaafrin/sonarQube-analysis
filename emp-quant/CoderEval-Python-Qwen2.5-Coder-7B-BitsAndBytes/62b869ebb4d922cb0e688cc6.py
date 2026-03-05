for item in response:
    if isinstance(item, dict):
        for key, value in item.items():
            if key not in last_applied_manifest:
                last_applied_manifest.append({key: value})
            else:
                update_last_applied_manifest_list_from_resp(last_applied_manifest[key], observer_schema, [value])
    elif isinstance(item, list):
        for sub_item in item:
            update_last_applied_manifest_list_from_resp(last_applied_manifest, observer_schema, [sub_item])