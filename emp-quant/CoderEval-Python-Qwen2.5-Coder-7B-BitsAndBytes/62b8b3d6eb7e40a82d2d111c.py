from typing import List, Union, Tuple, Any

class Declaration:
    pass

class Interface:
    pass

class ImplementsSpec:
    pass

def _normalizeargs(sequence: Union[List[Union[Declaration, Tuple[Any], Interface]], Tuple[Union[Declaration, Tuple[Any], Interface]]], output: List[Union[Declaration, Interface]] = None) -> List[Union[Declaration, Interface]]:
    if output is None:
        output = []

    for item in sequence:
        if isinstance(item, Declaration):
            output.append(item)
        elif isinstance(item, tuple):
            for sub_item in item:
                if isinstance(sub_item, Declaration):
                    output.append(sub_item)
                else:
                    raise ValueError("Tuple contains non-Declaration items")
        elif isinstance(item, Interface):
            output.append(item)
        elif isinstance(item, ImplementsSpec):
            output.extend(_normalizeargs(item.specs))
        else:
            raise ValueError(f"Unsupported type: {type(item)}")

    return output