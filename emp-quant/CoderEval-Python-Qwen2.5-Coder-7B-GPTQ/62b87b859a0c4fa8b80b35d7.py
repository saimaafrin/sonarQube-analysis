import warnings

warnings.warn("to_csv is not used.", DeprecationWarning)

def to_csv(self, separator=",", header=None):
    """
    Convert graph's points to CSV.

    *separator* delimits values, the default is comma.

    *header*, if not `None`, is the first string of the output
    (new line is added automatically).

    Since a graph can be multidimensional,
    for each point first its coordinate is converted to string
    (separated by *separator*), then each part of its value.

    To convert :class:`Graph` to CSV inside a Lena sequence,
    use :class:`lena.output.ToCSV`.
    """
    pass