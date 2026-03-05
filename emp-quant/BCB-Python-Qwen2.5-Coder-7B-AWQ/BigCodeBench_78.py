import csv
import io
from django.http import HttpRequest, FileResponse
def task_func(request, header, csv_data):
    # Create a StringIO object to hold the CSV data
    output = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.writer(output)
    
    # Write the header to the CSV file
    writer.writerow(header)
    
    # Write the CSV data to the CSV file
    for row in csv_data:
        writer.writerow(row)
    
    # Get the CSV data as a string
    csv_data = output.getvalue()
    
    # Close the StringIO object
    output.close()
    
    # Create a FileResponse object with the CSV data
    response = FileResponse(io.BytesIO(csv_data.encode('utf-8')), content_type='text/csv')
    
    # Set the content disposition to attachment
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    return response