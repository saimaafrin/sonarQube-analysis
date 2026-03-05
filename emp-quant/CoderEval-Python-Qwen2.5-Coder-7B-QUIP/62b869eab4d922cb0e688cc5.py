for field, value in observer_schema.items():
    if field not in last_applied_manifest:
        last_applied_manifest[field] = value
    if field in response:
        last_applied_manifest[field] = response[field]