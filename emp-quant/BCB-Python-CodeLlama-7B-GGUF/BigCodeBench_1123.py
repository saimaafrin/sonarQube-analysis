
import re
import urllib.parse
import ssl
import socket

def task_func(myString):
    # Compile regular expression to match HTTPS URLs
    https_regex = re.compile(r'https?://\S+')

    # Create dictionary to store SSL certificate expiry dates
    ssl_certs = {}

    # Iterate over all URLs in the string
    for url in https_regex.findall(myString):
        # Parse URL and retrieve domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc

        # Create SSL context with default settings
        context = ssl.create_default_context()

        # Connect to the domain and retrieve SSL certificate
        try:
            with context.wrap_socket(socket.socket(), server_hostname=domain) as s:
                s.connect((domain, 443))
                cert = s.getpeercert()
                expiry_date = ssl.cert_time_to_seconds(cert['notAfter'])
                ssl_certs[domain] = expiry_date
        except ssl.SSLError:
            # Ignore SSL errors and continue with next URL
            continue

    return ssl_certs