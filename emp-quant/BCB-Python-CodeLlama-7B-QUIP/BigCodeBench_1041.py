
import re
import os

def task_func(request):
    # Extract the filename from the request
    filename = re.search(r'/([^/]+)$', request).group(1)

    # Check if the file exists in the server's directory
    if os.path.isfile(filename):
        # Open the file and read its contents
        with open(filename, 'r') as f:
            file_content = f.read()

        # Return a 200 OK response with the file content
        return '200 OK', len(file_content), file_content
    else:
        # Return a 404 Not Found response
        return '404 Not Found', 0, ''