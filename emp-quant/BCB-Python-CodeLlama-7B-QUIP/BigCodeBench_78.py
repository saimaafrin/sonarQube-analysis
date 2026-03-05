
import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request, header, csv_data):
    # Create a file-like object with the CSV data
    csv_file = io.StringIO(csv_data)

    # Create the CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(csv_data)

    # Create a Django FileResponse object
    file_response = FileResponse(csv_file)

    # Set the content type to CSV
    file_response['Content-Type'] = 'text/csv'

    # Set the filename to the CSV file
    file_response['Content-Disposition'] = 'attachment; filename="my_data.csv"'

    return file_response