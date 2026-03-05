def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
# BEGIN SOLUTION
	if not isinstance(hist, histogram):
		hist = histogram(hist)

	graph = Graph(field_names=field_names, scale=scale)

	for bin_ in hist:
		x = getattr(bin_, get_coordinate)
		y = make_value(bin_)
		graph.append((x, y))

	return graph
	# END SOLUTION