for field in observer_schema:
    if isinstance(field, list):
        for sub_field in field:
            if sub_field not in last_applied_manifest:
                last_applied_manifest.append(sub_field)
    else:
        if field not in last_applied_manifest:
            last_applied_manifest.append(field)