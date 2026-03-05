import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings
def task_func(request, file_paths):
    # Create an in-memory file-like object to hold the ZIP data
    zip_buffer = io.BytesIO()
    
    # Create a ZIP file in memory
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for file_path in file_paths:
            # Add each file to the ZIP archive
            zipf.write(file_path, arcname=file_path.split('/')[-1])
    
    # Set the buffer position to the beginning of the file
    zip_buffer.seek(0)
    
    # Create a FileResponse object with the ZIP data
    response = FileResponse(zip_buffer, as_attachment=True, filename='files.zip')
    
    return response