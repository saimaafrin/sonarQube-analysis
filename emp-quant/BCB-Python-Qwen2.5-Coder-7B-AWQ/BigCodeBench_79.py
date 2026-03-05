import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings
def task_func(request, file_paths):
    # Create a BytesIO object to hold the ZIP file data
    zip_buffer = io.BytesIO()
    
    # Create a ZIP file in memory
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for file_path in file_paths:
            # Check if the file exists and is accessible
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            
            # Add the file to the ZIP archive
            zipf.write(file_path, os.path.basename(file_path))
    
    # Set the buffer position to the beginning of the file
    zip_buffer.seek(0)
    
    # Create a FileResponse object with the ZIP file data
    response = FileResponse(zip_buffer, as_attachment=True, filename='downloaded_files.zip')
    
    return response