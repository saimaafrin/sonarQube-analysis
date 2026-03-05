
import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create a new ZIP file in memory
    zip_file = io.BytesIO()
    with zipfile.ZipFile(zip_file, 'w') as zf:
        # Add the specified files to the ZIP file
        for file_path in file_paths:
            zf.write(file_path)
    # Return the ZIP file as an attachment
    return FileResponse(zip_file, as_attachment=True, filename='files.zip')