
import csv
import io

def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Open the CSV file in the specified encoding
    with open(filename, 'r', encoding=from_encoding) as f:
        # Create a CSV reader with the specified delimiter
        reader = csv.reader(f, delimiter=delimiter)
        # Read the CSV data as a list of dictionaries
        data = list(reader)

    # Convert the CSV data to the specified encoding
    converted_data = io.open(filename, 'w', encoding=to_encoding)
    converted_data.write(data)
    converted_data.close()

    # Return the list of dictionaries and the converted CSV data as a string
    return data, converted_data.getvalue()