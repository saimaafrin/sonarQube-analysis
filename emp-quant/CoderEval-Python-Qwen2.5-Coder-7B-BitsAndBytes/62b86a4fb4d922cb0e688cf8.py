import re

def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.
    """
    if isinstance(value, str):
        pattern = r'^[a-zA-Z0-9]+$'  # Example pattern: alphanumeric characters only
        return bool(re.match(pattern, value))
    elif isinstance(value, int):
        pattern = r'^\d+$'  # Example pattern: digits only
        return bool(re.match(pattern, str(value)))
    else:
        raise ValueError("Unsupported data type")