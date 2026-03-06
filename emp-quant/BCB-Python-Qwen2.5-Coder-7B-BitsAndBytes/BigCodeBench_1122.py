
import re
import socket
import urllib.parse

def task_func(myString):
    # Regular expression to find URLs in the string
    url_pattern = re.compile(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    # Find all URLs in the input string
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain and corresponding IP address
    result_dict = {}
    
    for url in urls:
        try:
            # Parse the URL to get the network location part
            parsed_url = urllib.parse.urlparse(url)
            domain = parsed_url.netloc
            
            # Get the IP address of the domain
            ip_address = socket.gethostbyname(domain)
            
            # Store the domain and IP address in the dictionary
            result_dict[domain] = ip_address
        except socket.gaierror:
            # If the domain cannot be resolved, set the IP address to None
            result_dict[domain] = None
    
    return result_dict