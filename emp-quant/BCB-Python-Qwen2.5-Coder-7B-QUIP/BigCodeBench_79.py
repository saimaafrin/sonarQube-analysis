
import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create an in-memory zip file
    output = io.BytesIO()
    with zipfile.ZipFile(output, mode='w') as zipf:
        for file_path in file_paths:
            # Assuming file_path is a relative path to the file in the media root
            zipf.write(os.path.join(settings.MEDIA_ROOT, file_path), arcname=file_path)

    # Set the content type and attachment header for the response
    response = FileResponse(output, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="files.zip"'

    return response