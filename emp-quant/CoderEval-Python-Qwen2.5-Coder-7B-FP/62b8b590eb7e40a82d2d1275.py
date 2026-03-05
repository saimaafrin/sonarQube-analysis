def _legacy_mergeOrderings(orderings):
seen = set()
	result = []
	for ordering in orderings:
		for element in ordering:
			if element not in seen:
				seen.add(element)
				result.append(element)
	return result