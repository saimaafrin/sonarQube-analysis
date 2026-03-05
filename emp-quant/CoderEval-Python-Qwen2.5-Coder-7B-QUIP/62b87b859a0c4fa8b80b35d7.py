import csv

def to_csv(self, separator=",", header=None):
    """
    Convert graph's points to CSV.

    *separator* delimits values, the default is comma.

    *header*, if not ``None``, is the first string of the output
    (new line is added automatically).

    Since a graph can be multidimensional,
    for each point first its coordinate is converted to string
    (separated by *separator*), then each part of its value.

    To convert :class:`Graph` to CSV inside a Lena sequence,
    use :class:`lena.output.ToCSV`.
    """
    # Assuming self is a graph object with points
    points = self.get_points()
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=separator)
        if header is not None:
            writer.writerow(header)
        for point in points:
            writer.writerow([str(coord) for coord in point])