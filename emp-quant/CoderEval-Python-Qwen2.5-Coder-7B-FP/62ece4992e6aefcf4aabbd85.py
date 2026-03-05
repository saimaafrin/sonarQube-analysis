def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
# If no roots are provided, initialize an empty set
	if roots is None:
		roots = set()

	# Iterate over each node in the graph
	for node in graph.subjects():
		# Check if there are any triples where the current node is the object and the property is the given property
		if not graph.objects(node, prop):
			# If no such triples exist, add the current node to the roots set
			roots.add(node)

	# Recursively call the function for each root found
	for root in roots.copy():
		find_roots(graph, prop, roots)

	return roots
```

This code defines a function `find_roots` that takes three arguments: a graph, a property, and an optional set of roots. The function returns a set of nodes that are considered roots in some sort of transitive hierarchy. The function assumes that the graph contains triples of the form `(child, prop, parent)`, where `prop` is the given property. The function iterates over each node in the graph and checks if there are any triples where the current node is the object and the property is the given property. If no such triples exist, the current node is added to the roots set. The function then recursively calls itself for each root found until no more roots can be found. Finally, the function returns the set of roots.