
import re
import os

def task_func(request):
    # Define the base directory where files are stored
    BASE_DIR = '/path/to/your/static/files'
    
    # Extract the filename from the request URL
    match = re.search(r'/([^?]+)', request)
    if not match:
        return "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
    
    filename = match.group(1)
    filepath = os.path.join(BASE_DIR, filename)
    
    # Check if the file exists
    if not os.path.isfile(filepath):
        return f"HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
    
    # Read the file content
    try:
        with open(filepath, 'rb') as file:
            file_content = file.read()
            content_length = len(file_content)
            return f"HTTP/1.1 200 OK\r\nContent-Length: {content_length}\r\n\r\n{file_content.decode('utf-8')}"
    except Exception as e:
        return f"HTTP/1.1 500 Internal Server Error\r\nContent-Length: 0\r\n\r\n"