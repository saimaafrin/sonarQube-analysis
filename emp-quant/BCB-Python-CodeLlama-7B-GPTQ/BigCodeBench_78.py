import csv
import io
from django.http import HttpRequest, FileResponse
def task_func(request, header, csv_data):
    """
    Generates a CSV file response from a Django HttpRequest.
    Constructs a CSV file using the provided header and CSV data,
    and sends it back as a Django FileResponse.
    This function is particularly useful in scenarios where you need to provide a downloadable CSV file in response to a user request on a Django web application.
    """
    # Create a CSV file object
    csv_file = io.StringIO()

    # Write the header to the CSV file
    csv_file.write(header)

    # Write the CSV data to the CSV file
    csv_file.write(csv_data)

    # Create a Django FileResponse object
    file_response = FileResponse(csv_file.getvalue(), as_attachment=True)

    # Set the filename of the CSV file
    file_response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return file_response