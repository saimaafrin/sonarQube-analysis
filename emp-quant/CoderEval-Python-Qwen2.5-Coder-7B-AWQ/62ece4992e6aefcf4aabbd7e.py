import os

def _resolve_string(matcher):
    name = matcher.group('name')
    default = matcher.group('default')
    
    if name in os.environ:
        return os.environ[name]
    elif default is not None:
        return default
    else:
        raise ValueError(f"Environment variable '{name}' is not set and no default value provided.")