from collections.abc import Mapping

def deep_merge_nodes(nodes):
    result = {}
    for node in nodes:
        for key, value in node.items():
            if key in result and isinstance(result[key], Mapping) and isinstance(value, Mapping):
                result[key] = deep_merge_nodes([result[key], value])
            else:
                result[key] = value
    return result