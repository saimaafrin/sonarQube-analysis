
import re
import urllib.parse
import ssl
import socket
from datetime import datetime

def task_func(myString):
    # Regular expression to find URLs
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain and SSL certificate expiry date
    result = {}
    
    # Create a default SSL context
    context = ssl.create_default_context()
    
    for url in urls:
        try:
            # Parse the URL to get the domain
            parsed_url = urllib.parse.urlparse(url)
            domain = parsed_url.netloc
            
            # Connect to the URL and get the SSL certificate
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    # Extract the expiration date from the certificate
                    expiry_date = cert['notAfter']
                    expiry_date_utc = datetime.strptime(expiry_date, '%b %d %H:%M:%S %Y %Z')
                    
                    # Store the domain and expiry date in the dictionary
                    result[domain] = expiry_date_utc
        except (ssl.SSLError, socket.gaierror, urllib.parse.InvalidURL):
            # Ignore SSL errors and invalid URLs
            continue
    
    return result