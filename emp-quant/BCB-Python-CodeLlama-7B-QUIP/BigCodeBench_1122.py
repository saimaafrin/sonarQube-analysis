
import re
import socket
import urllib.parse

def task_func(myString):
    # Create a dictionary to store the domains and their corresponding IP addresses
    domain_ip_dict = {}

    # Extract all URLs from the input string
    urls = re.findall(r"https?://(?:[\w-]+.)+", myString)

    for url in urls:
        # Parse the URL to get the domain
        domain = urllib.parse.urlparse(url).netloc

        try:
            # Resolve the domain to get its IP address
            ip_address = socket.gethostbyn(domain)

            # Add the domain and IP address to the dictionary
            domain_ip_dict[domain] = ip_address
        except socket.gaierror:
            # If the domain cannot be resolved, add None to the dictionary
            domain_ip_dict[domain] = None

    return domain_ip_dict