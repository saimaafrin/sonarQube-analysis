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
    # Create a regular expression to match URLs
    url_regex = re.compile(
        r'https?://'  # Match either http or https
        r'(?:[\w.-]+)\.'  # Match a domain name
        r'(?:com|org|net|gov|edu|mil|biz|info|name|pro|aero|coop|museum|[a-zA-Z]{2})'  # Match a TLD
        r'(?::\d+)?'  # Match a port number
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Create a dictionary to store the results
    results = {}

    # Iterate over the URLs in the string
    for url in url_regex.findall(myString):
        # Extract the domain name from the URL
        domain = urllib.parse.urlparse(url).netloc

        # Try to retrieve the SSL certificate for the domain
        try:
            # Create an SSL context
            context = ssl.create_default_context()

            # Connect to the domain
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((domain, 443))

            # Get the SSL certificate
            cert = context.wrap_socket(s, server_hostname=domain)

            # Get the expiration date of the SSL certificate
            expiration_date = cert.get_expiration_date()

            # Add the domain and expiration date to the results dictionary
            results[domain] = expiration_date

        # If there is an SSL error, ignore the URL and continue
        except ssl.SSLError:
            continue

    # Return the results dictionary
    return results
myString = "This is a string with some URLs: https://www.example.com, https://www.example2.com, http://www.example3.com"