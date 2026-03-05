import re

def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.
    """
    if re.match(r'^[a-zA-Z0-9]+$', value):
        return True
    else:
        return False