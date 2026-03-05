import re
import socket
import urllib.parse
def task_func(myString):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain and its corresponding IP address
    result = {}
    
    for url in urls:
        try:
            # Parse the URL to extract the domain
            parsed_url = urllib.parse.urlparse(url)
            domain = parsed_url.netloc
            
            # Get the IP address of the domain
            ip_address = socket.gethostbyname(domain)
            result[domain] = ip_address
        except socket.gaierror:
            # If the domain cannot be resolved, add None as the IP address
            result[domain] = None
    
    return result