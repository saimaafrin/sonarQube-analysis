def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    default_schema = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            default_schema[key] = generate_default_observer_schema_dict(value, True)
        elif isinstance(value, list):
            default_schema[key] = [generate_default_observer_schema_dict(item, True) if isinstance(item, dict) else item for item in value]
        else:
            default_schema[key] = None
    return default_schema