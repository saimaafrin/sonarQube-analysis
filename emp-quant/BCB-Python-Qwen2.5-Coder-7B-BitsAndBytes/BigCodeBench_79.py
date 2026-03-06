
import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create a BytesIO buffer to hold the zip data
    zip_buffer = io.BytesIO()
    
    # Create a ZipFile object using the BytesIO buffer
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for file_path in file_paths:
            # Check if the file exists and is accessible
            if os.path.exists(file_path) and os.access(file_path, os.R_OK):
                # Add the file to the zip archive
                zipf.write(file_path, arcname=os.path.basename(file_path))
    
    # Set the buffer position to the beginning of the file
    zip_buffer.seek(0)
    
    # Create a FileResponse object with the zip data
    response = FileResponse(zip_buffer, as_attachment=True, filename='files.zip')
    
    return response