def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
    """
    if isinstance(manifest_dict, dict):
        new_dict = {}
        for key, value in manifest_dict.items():
            if isinstance(value, dict):
                new_dict[key] = generate_default_observer_schema_dict(value, True)
            elif isinstance(value, list):
                new_dict[key] = [generate_default_observer_schema_dict(item, True) for item in value]
            else:
                new_dict[key] = value
        return new_dict
    elif isinstance(manifest_dict, list):
        return [generate_default_observer_schema_dict(item, True) for item in manifest_dict]
    else:
        return manifest_dict