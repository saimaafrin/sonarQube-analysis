def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    default_schema = {}
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            default_schema[key] = generate_default_observer_schema_dict(value, first_level=True)
        elif isinstance(value, list):
            default_schema[key] = [generate_default_observer_schema_dict(item, first_level=True) if isinstance(item, dict) else item for item in value]
        else:
            default_schema[key] = value
    if first_level:
        return {key: {"default": value} for key, value in default_schema.items()}
    return default_schema