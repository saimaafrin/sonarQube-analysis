import os

def _resolve_string(matcher):
    name = matcher.group('name')
    default = matcher.group('default')
    value = os.getenv(name)
    if value is None and default is None:
        raise ValueError(f"Environment variable '{name}' is not set and no default value provided.")
    return value if value is not None else default