from collections import Counter

def _dictsum(dicts):
    combined = Counter()
    for d in dicts:
        combined += Counter(d)
    return dict(combined)