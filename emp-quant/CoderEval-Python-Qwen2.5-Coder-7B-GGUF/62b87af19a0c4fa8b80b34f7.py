def difference(d1, d2, level=-1):
    if level == 0:
        return {}
    result = {}
    for key, value in d1.items():
        if key not in d2:
            result[key] = value
        elif isinstance(value, dict) and isinstance(d2[key], dict):
            result[key] = difference(value, d2[key], level - 1)
    return result