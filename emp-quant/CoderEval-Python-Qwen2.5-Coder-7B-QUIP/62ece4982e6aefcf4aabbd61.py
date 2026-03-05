from collections import defaultdict

def _dictsum(dicts):
    result = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            result[key] += value
    return dict(result)