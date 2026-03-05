
import re
import socket
import urllib.parse

def task_func(myString):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain and IP address
    result = {}
    
    for url in urls:
        # Parse the URL to extract the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        try:
            # Get the IP address of the domain
            ip_address = socket.gethostbyname(domain)
            result[domain] = ip_address
        except socket.gaierror:
            # If the domain cannot be resolved, set the IP address to None
            result[domain] = None
    
    return result