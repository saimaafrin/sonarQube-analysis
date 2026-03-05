
import re
import os

def task_func(request):
    # Extract the filename from the request
    filename = request.split(' ')[1].split('/')[-1]
    
    # Check if the filename is valid
    if not re.match(r'^[a-zA-Z0-9_]+\.[a-zA-Z0-9]+$', filename):
        return "400 Bad Request"
    
    # Check if the file exists in the server's directory
    if not os.path.exists(filename):
        return "404 Not Found"
    
    # Read the file content
    with open(filename, 'r') as file:
        content = file.read()
    
    # Return the HTTP response
    return f"200 OK\nContent-Length: {len(content)}\n\n{content}"