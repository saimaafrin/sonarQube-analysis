
import re
import os

def task_func(request):
    # Extract the filename from the request
    filename = re.search(r'/([^/]+)$', request).group(1)

    # Check if the file exists in the server's directory
    if not os.path.isfile(filename):
        return 'File not found'

    # Open the file and read its contents
    with open(filename, 'r') as f:
        content = f.read()

    # Return an HTTP response with the file content
    return 'HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}'.format(len(content), content)