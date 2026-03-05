from typing import Set, Tuple

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    in_code_block = False
    new_text = []
    for line in text.split('\n'):
        if '