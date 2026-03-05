import re
import os
def task_func(request):
    # Extract the filename from the request
    filename = re.search(r'/([^/]+)$', request.path).group(1)

    # Check if the file exists in the server's directory
    if not os.path.isfile(filename):
        return 'File not found', 404

    # Open the file and read its content
    with open(filename, 'r') as f:
        content = f.read()

    # Return the file content with a 200 OK status code
    return content, 200
request = 'GET /file.txt HTTP/1.1'