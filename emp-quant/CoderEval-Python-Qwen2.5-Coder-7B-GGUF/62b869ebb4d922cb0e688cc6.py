def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    for item in observer_schema:
        if isinstance(item, dict):
            if item['name'] in response:
                update_last_applied_manifest_dict_from_resp(
                    last_applied_manifest, item['schema'], response[item['name']]
                )
            else:
                last_applied_manifest.append({item['name']: None})
        elif isinstance(item, list):
            if item['name'] in response:
                update_last_applied_manifest_list_from_resp(
                    last_applied_manifest, item['schema'], response[item['name']]
                )
            else:
                last_applied_manifest.append({item['name']: []})
        else:
            if item in response:
                last_applied_manifest.append({item: response[item]})
            else:
                last_applied_manifest.append({item: None})