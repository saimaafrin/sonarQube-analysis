import re

def regex_dict(item):
    return {re.compile(k): v for k, v in item.items()}