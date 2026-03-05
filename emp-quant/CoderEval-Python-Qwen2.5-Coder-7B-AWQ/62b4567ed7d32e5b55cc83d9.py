from collections import Mapping

def deep_merge_nodes(nodes):
    if not nodes:
        return {}
    
    merged = {}
    for node in nodes:
        if isinstance(node, Mapping):
            for key, value in node.items():
                if key in merged and isinstance(merged[key], Mapping) and isinstance(value, Mapping):
                    merged[key] = deep_merge_nodes([merged[key], value])
                else:
                    merged[key] = value
        else:
            raise ValueError("All elements must be Mappings")
    
    return merged