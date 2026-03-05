for field in observer_schema:
    if field['type'] == 'list':
        for item in response:
            if item not in last_applied_manifest:
                last_applied_manifest.append(item)
    elif field['type'] == 'dict':
        for key, value in field['properties'].items():
            if key not in last_applied_manifest or value != last_applied_manifest[key]:
                last_applied_manifest[key] = value
    else:
        if field['name'] not in last_applied_manifest or response[field['name']] != last_applied_manifest[field['name']]:
            last_applied_manifest[field['name']] = response[field['name']]