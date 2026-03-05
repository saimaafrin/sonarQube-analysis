
import re
import os

def task_func(request):
    # Define the directory where static files are stored
    static_dir = 'path/to/static/files'
    
    # Extract the filename from the request
    filename = re.search(r'GET /(\S+) HTTP/1.1', request).group(1)
    
    # Check if the filename is valid (e.g., no directory traversal)
    if '..' in filename or not filename:
        return "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
    
    # Construct the full path to the file
    file_path = os.path.join(static_dir, filename)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        return "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
    
    # Read the file content
    with open(file_path, 'rb') as file:
        content = file.read()
    
    # Get the content length
    content_length = len(content)
    
    # Return the HTTP response
    return f"HTTP/1.1 200 OK\r\nContent-Length: {content_length}\r\n\r\n{content.decode('utf-8')}"