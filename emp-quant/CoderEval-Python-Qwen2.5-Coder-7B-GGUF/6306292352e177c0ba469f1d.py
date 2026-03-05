from typing import Set, Tuple

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    in_code_block = False
    result = []
    current_tag = []

    for char in text:
        if char == '`':
            in_code_block = not in_code_block
        elif char == '<' and not in_code_block:
            current_tag.append(char)
        elif char == '>' and not in_code_block:
            current_tag.append(char)
            tag = ''.join(current_tag)
            tags.add(tag)
            current_tag = []
        elif current_tag:
            current_tag.append(char)

    if replacer:
        result = ''.join(replacer(tag) if tag in tags else tag for tag in text.split('<') if '>' in tag)
    else:
        result = text

    return tags, result