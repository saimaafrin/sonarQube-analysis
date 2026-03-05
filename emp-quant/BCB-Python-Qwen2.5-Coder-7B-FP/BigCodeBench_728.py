import csv
import io
def task_func(filename='sample.csv', from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Read the CSV file with the specified encoding
    with open(filename, 'r', encoding=from_encoding) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data_list = [row for row in reader]
    
    # Convert the CSV data to the specified encoding
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data_list[0].keys(), delimiter=delimiter)
    writer.writeheader()
    writer.writerows(data_list)
    converted_csv = output.getvalue()
    
    # Reset the StringIO buffer
    output.close()
    
    return data_list, converted_csv