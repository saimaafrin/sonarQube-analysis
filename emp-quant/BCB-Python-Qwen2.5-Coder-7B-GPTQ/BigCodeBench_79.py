import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings
def task_func(request, file_paths):
    # Create an in-memory zip file
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for file_path in file_paths:
            # Add each file to the zip file
            zipf.write(file_path, arcname=file_path.split('/')[-1])
    
    # Set the buffer position to the beginning
    zip_buffer.seek(0)
    
    # Create a FileResponse object with the zip file
    response = FileResponse(zip_buffer, as_attachment=True, filename='files.zip')
    
    return response