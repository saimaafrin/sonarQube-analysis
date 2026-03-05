import csv
import io
def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    """
    Convert the encoding of a CSV file from one encoding to another and return a list of dictionaries along with the converted CSV data as a string.
    """
    # Open the CSV file
    with open(filename, 'r', encoding=from_encoding) as f:
        # Create a CSV reader
        reader = csv.reader(f, delimiter=delimiter)
        # Create a list of dictionaries
        data = []
        # Read the CSV file
        for row in reader:
            # Create a dictionary for the current row
            row_dict = {}
            # Add the row data to the dictionary
            for i, col in enumerate(row):
                row_dict[i] = col
            # Add the dictionary to the list
            data.append(row_dict)
        # Convert the CSV data to a string
        csv_data = io.StringIO()
        writer = csv.writer(csv_data, delimiter=delimiter)
        writer.writerows(data)
        # Return the list of dictionaries and the converted CSV data as a string
        return data, csv_data.getvalue()
filename = 'sample.csv'
from_encoding = 'cp1251'
to_encoding = 'utf8'
delimiter = ','