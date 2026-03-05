
import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request, header, csv_data):
    # Create a CSV file object
    csv_file = io.StringIO()

    # Write the header to the CSV file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)

    # Write the CSV data to the CSV file
    for row in csv_data:
        csv_writer.writerow(row)

    # Create a Django FileResponse object from the CSV file
    file_response = FileResponse(csv_file.getvalue(), as_attachment=True)

    # Set the filename for the CSV file
    file_response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return file_response