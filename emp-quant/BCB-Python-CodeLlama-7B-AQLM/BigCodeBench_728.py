import csv
import io
def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    """
    Convert the encoding of a CSV file from one encoding to another and return a list of dictionaries along with the converted CSV data as a string.
    
    Parameters:
    - filename (str): The name of the CSV file.
    - from_encoding (str): The original encoding of the CSV file. Default is 'cp1251'.
    - to_encoding (str): The encoding to which the CSV file should be converted. Default is 'utf8'.
    - delimiter (str): The character that separates the fields in the CSV file. Default is ','.
    
    Returns:
    tuple: A tuple containing:
        - list: A list of dictionaries. Each dictionary represents a row in the CSV file.
        - str: The converted CSV data as a string.
    
    Requirements:
    - csv
    - io
    
    Example:
    >>> data, converted_csv = task_func('sample.csv', 'cp1251', 'utf8')
    >>> print(data)
    [{'Name': 'Alice', 'Age': '30'}, {'Name': 'Bob', 'Age': '25'}]
    >>> print(converted_csv)
    "Name,Age\nAlice,30\nBob,25\n"
    
    Note:
    - The default filename to use if not specified is 'sample.csv'.
    - The default delimiter is ','.
    """
    # Open the CSV file.
    with io.open(filename, 'r', encoding=from_encoding) as f:
        # Create a CSV reader object.
        reader = csv.reader(f, delimiter=delimiter)
        # Create a list of dictionaries.
        data = []
        # Iterate over the rows in the CSV file.
        for row in reader:
            # Create a dictionary for the current row.
            row_dict = {}
            # Iterate over the fields in the current row.
            for i in range(len(row)):
                # Add the field to the dictionary.
                row_dict[reader.fieldnames[i]] = row[i]
            # Add the dictionary to the list.
            data.append(row_dict)
        # Convert the CSV data to a string.
        converted_csv = io.StringIO()
        # Create a CSV writer object.
        writer = csv.writer(converted_csv, delimiter=delimiter)
        # Write the CSV data to the string.
        writer.writerows(data)
        # Return the list of dictionaries and the converted CSV data as a string.
        return data, converted_csv.getvalue()