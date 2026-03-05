import re

def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.
    """
    if isinstance(value, str):
        pattern = r'^[a-zA-Z0-9]+$'  # Example pattern: alphanumeric string
        return re.match(pattern, value) is not None
    elif isinstance(value, int):
        pattern = r'^\d+$'  # Example pattern: integer
        return re.match(pattern, str(value)) is not None
    elif isinstance(value, float):
        pattern = r'^\d+\.\d+$'  # Example pattern: float
        return re.match(pattern, str(value)) is not None
    else:
        return False