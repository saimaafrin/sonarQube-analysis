import re
import os
def task_func(request):
    # Define the base directory where files are stored
    base_dir = '/path/to/static/files'
    
    # Extract the filename from the request
    filename = re.search(r'GET /([^ ]+) HTTP/1.1', request).group(1)
    
    # Construct the full path to the file
    file_path = os.path.join(base_dir, filename)
    
    # Check if the file exists and is a regular file
    if os.path.isfile(file_path):
        # Read the content of the file
        with open(file_path, 'rb') as file:
            content = file.read()
            # Return a 200 OK response with the content length and file content
            return f'HTTP/1.1 200 OK\nContent-Length: {len(content)}\n\n{content}'
    else:
        # Return a 404 Not Found response
        return 'HTTP/1.1 404 Not Found\n\nFile not found.'