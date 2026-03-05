import re
import urllib.parse
import ssl
import socket
def task_func(myString):
    """
    Extracts all URLs from a string and retrieves the domain and the expiration date of the SSL certificate for each HTTPS URL.
    Only HTTPS URLs are processed; HTTP URLs are ignored.
    The function handles SSL errors by ignoring any HTTPS URLs where the SSL certificate cannot be retrieved due to such errors, and these domains are not included in the returned dictionary.
    The function should output with:
        dict: A dictionary with domains as keys and SSL certificate expiry dates in UTC format as values.
        The dictionary includes only those HTTPS URLs for which the SSL certificate was successfully retrieved.
        Domains with SSL errors are excluded.
    """
    # Compile regular expression to match URLs
    url_regex = re.compile(r'https?://\S+')

    # Create dictionary to store results
    results = {}

    # Iterate over URLs in the input string
    for url in url_regex.findall(myString):
        # Parse URL and extract domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc

        # Check if URL is HTTPS
        if parsed_url.scheme == 'https':
            # Create SSL context with default settings
            context = ssl.create_default_context()

            # Create socket and connect to URL
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((domain, 443))

            # Get SSL certificate expiration date
            try:
                cert = ssl.get_server_certificate((domain, 443), context=context)
                expiry_date = ssl.cert_time_to_seconds(cert.get_notAfter())
            except ssl.SSLError:
                # Ignore SSL errors and continue
                continue

            # Add domain and expiration date to results dictionary
            results[domain] = expiry_date

    # Return results dictionary
    return results
myString = 'This is a string with some URLs: https://www.example1.com, https://www.example2.com, and https://www.example3.com'