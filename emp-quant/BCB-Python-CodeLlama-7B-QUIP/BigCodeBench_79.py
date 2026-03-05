
import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create a new ZipFile object
    zip_file = zipfile.ZipFile(mode="w", compression=zipfile.ZIP_DEFLATED)

    # Iterate over the file paths and add them to the ZipFile
    for file_path in file_paths:
        # Open the file in binary mode
        with open(file_path, "rb") as file:
            # Add the file to the ZipFile
            zip_file.write(file_path)

    # Return a FileResponse with the ZipFile as an attachment
    return FileResponse(zip_file, filename="files.zip")