def deep_merge_nodes(nodes):
    result = {}
    for node in nodes:
        for key, value in node.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge_nodes([result[key], value])
            else:
                result[key] = value
    return result