def _legacy_mergeOrderings(orderings):
    result = []
    for ordering in orderings:
        for item in ordering:
            if item not in result:
                result.append(item)
    return result