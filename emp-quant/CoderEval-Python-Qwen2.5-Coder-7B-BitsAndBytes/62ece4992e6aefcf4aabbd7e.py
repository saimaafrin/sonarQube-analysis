import os

def _resolve_string(matcher):
    name = matcher.group('name')
    default_value = matcher.group('default')
    
    if name in os.environ:
        return os.environ[name]
    elif default_value is not None:
        return default_value
    else:
        raise ValueError(f"Environment variable '{name}' is not set and no default value provided.")