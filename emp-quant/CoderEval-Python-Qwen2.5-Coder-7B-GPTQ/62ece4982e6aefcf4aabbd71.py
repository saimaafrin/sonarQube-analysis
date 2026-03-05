import re

def regex_dict(item):
    return {re.compile(key): value for key, value in item.items()}