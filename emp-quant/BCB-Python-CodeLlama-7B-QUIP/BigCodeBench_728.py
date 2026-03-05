
import csv
import io

def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Open the file with the specified encoding
    with open(filename, 'r', encoding=from_encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        # Convert the encoding to the specified encoding
        data = [row for row in reader]
        # Convert the data to a string
        data_str = ''.join(row for row in data)
        # Return the list of dictionaries and the converted data as a string
        return data, data_str