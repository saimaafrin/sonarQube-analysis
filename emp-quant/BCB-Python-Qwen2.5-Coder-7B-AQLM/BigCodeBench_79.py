
import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create an in-memory file-like object
    zip_buffer = io.BytesIO()
    
    # Create a ZIP file in memory
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for file_path in file_paths:
            # Ensure the file exists
            if not settings.MEDIA_ROOT.joinpath(file_path).exists():
                continue
            # Add file to the ZIP archive
            zipf.write(settings.MEDIA_ROOT.joinpath(file_path), arcname=file_path)
    
    # Set the buffer position to the beginning
    zip_buffer.seek(0)
    
    # Create a FileResponse object with the ZIP file
    response = FileResponse(zip_buffer, as_attachment=True, filename='files.zip')
    
    return response