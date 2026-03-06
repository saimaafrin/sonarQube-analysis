
import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request, header, csv_data):
    # Create an in-memory stream to hold the CSV content
    buffer = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.writer(buffer)
    
    # Write the header row
    writer.writerow(header)
    
    # Write the data rows
    for row in csv_data:
        writer.writerow(row)
    
    # Get the value of the StringIO buffer (CSV content)
    csv_content = buffer.getvalue()
    
    # Reset the buffer position to the beginning
    buffer.seek(0)
    
    # Create a FileResponse object with the CSV content
    response = FileResponse(buffer, as_attachment=True, filename='output.csv')
    
    return response