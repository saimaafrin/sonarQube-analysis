def to_csv(self, separator=",", header=None):
# TODO: remove this method from Graph class and use ToCSV instead
	if header:
		yield header + '\n'
	for point in self.points():
		line = [str(coord) for coord in point]
		line.extend(str(value) for value in point.values())
		yield separator.join(line) + '\n'