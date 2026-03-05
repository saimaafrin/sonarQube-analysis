import re

def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.
    """
    # Define a dictionary of regular expressions for different types of values
    regex_patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone': r'^\+?[1-9]\d{1,14}$',
        'url': r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
    }

    # Check if the value matches any of the defined patterns
    for key, pattern in regex_patterns.items():
        if re.match(pattern, value):
            return True

    return False