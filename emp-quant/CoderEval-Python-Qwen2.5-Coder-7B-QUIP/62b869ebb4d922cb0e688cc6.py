for field in observer_schema:
    if field not in last_applied_manifest:
        last_applied_manifest[field] = response[field]