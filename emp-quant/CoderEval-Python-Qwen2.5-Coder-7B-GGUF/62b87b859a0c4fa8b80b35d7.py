import warnings
warnings.warn("to_csv is not used in Lena 0.5. Convert graph's points to CSV using lena.output.ToCSV.", DeprecationWarning)

def to_csv(self, separator=",", header=None):
    if header is not None:
        yield header + '\n'
    for point in self.points:
        coordinates = [str(coord) for coord in point.coordinates]
        values = [str(value) for value in point.values]
        yield separator.join(coordinates + values) + '\n'