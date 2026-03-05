import re
from typing import Set, Tuple

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    code_block_pattern = re.compile(r'