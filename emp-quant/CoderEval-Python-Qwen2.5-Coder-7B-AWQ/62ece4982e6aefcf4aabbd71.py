import re

def regex_dict(item):
    return {re.compile(key.replace('*', '.*')): value for key, value in item.items()}