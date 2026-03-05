from typing import Set, Tuple

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    in_code_block = False
    new_text = []
    
    for line in text.split('\n'):
        parts = []
        i = 0
        while i < len(line):
            if not in_code_block:
                start = line.find('<', i)
                end = line.find('>', start + 1)
                if start != -1 and end != -1:
                    tag = line[start:end + 1]
                    tags.add(tag)
                    if replacer:
                        tag = replacer(tag)
                    parts.append(line[i:start] + tag)
                    i = end + 1
                else:
                    parts.append(line[i:])
                    break
            else:
                end = line.find('`', i)
                if end == -1:
                    parts.append(line[i:])
                    break
                else:
                    parts.append(line[i:end + 1])
                    i = end + 1
            if line[i:i+3] == '