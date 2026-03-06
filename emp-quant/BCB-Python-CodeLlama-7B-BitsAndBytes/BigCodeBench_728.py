
import csv
import io

def task_func(filename='sample.csv', from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Open the CSV file in the specified encoding
    with open(filename, 'r', encoding=from_encoding) as f:
        # Create a CSV reader
        reader = csv.reader(f, delimiter=delimiter)
        # Read the CSV data
        data = list(reader)
        # Convert the data to the specified encoding
        converted_data = [row.encode(to_encoding).decode(to_encoding) for row in data]
        # Return the list of dictionaries and the converted CSV data as a string
        return converted_data, converted_data.encode(to_encoding).decode(to_encoding)