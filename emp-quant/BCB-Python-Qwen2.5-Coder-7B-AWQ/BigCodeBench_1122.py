import re
import socket
import urllib.parse
def task_func(myString):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain and corresponding IP address
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
            # If the domain cannot be resolved, set IP address to None
            result[domain] = None
    
    return result