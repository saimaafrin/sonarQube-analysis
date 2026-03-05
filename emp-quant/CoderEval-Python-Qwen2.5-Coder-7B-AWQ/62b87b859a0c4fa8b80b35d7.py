import csv

def to_csv(self, separator=",", header=None):
    """
    .. deprecated:: 0.5 in Lena 0.5 to_csv is not used.
      Iterables are converted to tables.

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
    data = []
    for point in self.points:
        coord_str = separator.join(str(coord) for coord in point[0])
        value_str = separator.join(str(val) for val in point[1:])
        data.append([coord_str] + value_str)

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow([header])
        writer.writerows(data)