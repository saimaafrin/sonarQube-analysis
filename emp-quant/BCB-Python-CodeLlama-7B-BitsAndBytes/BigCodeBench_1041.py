
import re
import os

def task_func(request):
    # Extract the filename from the request
    filename = re.search(r'/([^/]+)$', request).group(1)

    # Check if the file exists in the server's directory
    if os.path.isfile(filename):
        # Read the file content
        with open(filename, 'r') as f:
            content = f.read()

        # Return a 200 OK response with the file content
        return 'HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}'.format(len(content), content)
    else:
        # Return a 404 Not Found response
        return 'HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n'