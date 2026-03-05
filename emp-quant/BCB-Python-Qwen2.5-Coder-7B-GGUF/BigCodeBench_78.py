
import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request: HttpRequest, header: list, csv_data: list) -> FileResponse:
    # Create a StringIO object to hold the CSV data
    output = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.writer(output)
    
    # Write the header to the CSV file
    writer.writerow(header)
    
    # Write the CSV data to the CSV file
    for row in csv_data:
        writer.writerow(row)
    
    # Get the value of the StringIO object and reset the cursor
    csv_file = output.getvalue()
    output.seek(0)
    
    # Create a FileResponse object with the CSV data
    response = FileResponse(output, content_type='text/csv')
    
    # Set the filename for the attachment
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    return response