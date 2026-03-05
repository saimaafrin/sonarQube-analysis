import csv
import io
from django.http import HttpRequest, FileResponse
def task_func(request, header, csv_data):
    # Create an in-memory file-like object
    output = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.writer(output)
    
    # Write the header to the CSV file
    writer.writerow(header)
    
    # Write the CSV data to the CSV file
    for row in csv_data:
        writer.writerow(row)
    
    # Get the value of the in-memory file-like object
    output.seek(0)
    csv_file = output.getvalue()
    
    # Create a FileResponse object with the CSV file as an attachment
    response = FileResponse(csv_file, as_attachment=True, filename='data.csv')
    
    return response