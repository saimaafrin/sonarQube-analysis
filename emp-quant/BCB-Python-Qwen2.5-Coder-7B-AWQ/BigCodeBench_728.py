import csv
import io
def task_func(filename='sample.csv', from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Read the CSV file with the specified encoding
    with open(filename, 'r', encoding=from_encoding) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = list(reader)
    
    # Convert the CSV data to the specified encoding
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=reader.fieldnames, delimiter=delimiter)
    writer.writeheader()
    writer.writerows(data)
    converted_csv = output.getvalue()
    
    # Return the list of dictionaries and the converted CSV data as a string
    return data, converted_csv