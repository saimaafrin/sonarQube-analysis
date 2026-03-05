import re
from typing import Set, Tuple

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    pattern = r'\b\w+'
    def replacer_func(match):
        tag = match.group()
        tags.add(tag)
        if replacer:
            return replacer(tag)
        return tag
    text = re.sub(pattern, replacer_func, text)
    return tags, text