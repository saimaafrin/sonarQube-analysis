
import re
import urllib.parse
import ssl
import socket

def task_func(myString):
    # Compile regular expression to match URLs
    url_regex = re.compile(r'https?://\S+')

    # Create dictionary to store SSL certificate expiry dates
    ssl_certs = {}

    # Iterate over all URLs in the string
    for url in url_regex.findall(myString):
        # Parse URL and extract domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc

        # Create SSL context with appropriate settings
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_REQUIRED

        # Try to retrieve SSL certificate
        try:
            conn = socket.create_connection((domain, 443))
            cert = conn.getpeercert()
            expiry_date = ssl.cert_time_to_seconds(cert['notAfter'])
            ssl_certs[domain] = expiry_date
        except ssl.SSLError:
            # Ignore SSL errors and continue with next URL
            continue
        except socket.gaierror:
            # Ignore non-HTTPS URLs
            continue

    return ssl_certs