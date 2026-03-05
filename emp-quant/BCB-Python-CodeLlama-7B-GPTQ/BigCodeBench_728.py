import csv
import io
def task_func(filename, from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    """
    Convert the encoding of a CSV file from one encoding to another and return a list of dictionaries along with the converted CSV data as a string.
    """
    # Open the CSV file in the specified encoding
    with open(filename, 'r', encoding=from_encoding) as f:
        # Create a CSV reader object
        reader = csv.reader(f, delimiter=delimiter)
        # Create a list of dictionaries to store the data
        data = []
        # Iterate over the rows in the CSV file
        for row in reader:
            # Create a dictionary to store the data for the current row
            row_dict = {}
            # Iterate over the columns in the current row
            for i, column in enumerate(row):
                # Add the column data to the dictionary
                row_dict[i] = column
            # Add the dictionary to the list of dictionaries
            data.append(row_dict)
        # Convert the CSV data to a string
        csv_data = io.StringIO()
        writer = csv.writer(csv_data, delimiter=delimiter)
        writer.writerows(data)
        csv_data = csv_data.getvalue()
    # Return the list of dictionaries and the converted CSV data as a string
    return data, csv_data