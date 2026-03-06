
import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create a ZIP file in memory
    zip_file = io.BytesIO()
    with zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in file_paths:
            # Add the file to the ZIP file
            zf.write(file_path)

    # Return a FileResponse with the ZIP file as an attachment
    return FileResponse(zip_file, as_attachment=True, filename='files.zip')