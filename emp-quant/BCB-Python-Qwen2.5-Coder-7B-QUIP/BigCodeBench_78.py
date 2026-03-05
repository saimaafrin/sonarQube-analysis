
import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request, header, csv_data):
    # Create a StringIO to hold the CSV data
    csv_buffer = io.StringIO()
    
    # Create a CSV writer object
    csv_writer = csv.writer(csv_buffer)
    
    # Write the header to the CSV
    csv_writer.writerow(header)
    
    # Write the data to the CSV
    for row in csv_data:
        csv_writer.writerow(row)
    
    # Seek to the beginning of the buffer to prepare for reading
    csv_buffer.seek(0)
    
    # Create a FileResponse object with the CSV data
    response = FileResponse(csv_buffer, content_type='text/csv', filename='data.csv')
    
    # Add a Content-Disposition header to the response to trigger the download
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    return response