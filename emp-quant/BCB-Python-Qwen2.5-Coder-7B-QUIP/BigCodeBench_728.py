
import csv
import io

def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Read the CSV file with the original encoding
    with open(filename, 'r', encoding=from_encoding) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = list(reader)
    
    # Convert the CSV data to the new encoding
    with io.StringIO() as buffer:
        writer = csv.DictWriter(buffer, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writerows(data)
        converted_csv = buffer.getvalue()
    
    # Return the list of dictionaries and the converted CSV data as a string
    return data, converted_csv