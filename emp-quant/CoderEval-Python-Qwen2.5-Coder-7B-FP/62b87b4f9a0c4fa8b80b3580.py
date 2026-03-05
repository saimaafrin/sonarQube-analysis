def integral(bins, edges):
# Calculate the width of each bin
	widths = np.diff(edges)
	
	# Calculate the height of each bin as the average value in that bin
	heights = (bins[:-1] + bins[1:]) / 2
	
	# Calculate the area of each bin and sum them up to get the total area
	area = np.sum(widths * heights)
	return area