import os

def _resolve_string(matcher):
    name = matcher.group('name')
    default_value = matcher.group('default_value')
    value = os.getenv(name)
    if value is None and default_value is None:
        raise ValueError(f"Environment variable '{name}' is not set and no default value is provided.")
    return value if value is not None else default_value