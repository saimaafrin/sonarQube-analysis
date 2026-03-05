import re
import urllib.parse
import ssl
import socket
def task_func(myString):
    """
    Extracts all URLs from a string and retrieves the domain and the expiration date of the SSL certificate for each HTTPS URL.
    Only HTTPS URLs are processed; HTTP URLs are ignored. The function handles SSL errors by ignoring any HTTPS URLs where the SSL certificate cannot be retrieved due to such errors, and these domains are not included in the returned dictionary.
    The function should output with:
        dict: A dictionary with domains as keys and SSL certificate expiry dates in UTC format as values.
        The dictionary includes only those HTTPS URLs for which the SSL certificate was successfully retrieved.
        Domains with SSL errors are excluded.
    """
    # Create a regular expression to match URLs
    url_regex = re.compile(
        r'https?://'  # Match http or https
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # Match domain name
        r'localhost|'  # Or match localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Or match IP address
        r'(?::\d+)?'  # Optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Create a dictionary to store the results
    results = {}

    # Iterate over the URLs in the input string
    for url in url_regex.findall(myString):
        # Skip HTTP URLs
        if not url.startswith('https://'):
            continue

        # Create a new SSL context
        context = ssl.create_default_context()

        # Connect to the URL and retrieve the SSL certificate
        try:
            with urllib.request.urlopen(url, context=context) as response:
                cert = response.getpeercert()
        except ssl.SSLError:
            # Ignore SSL errors
            continue

        # Extract the domain and expiration date from the SSL certificate
        domain = urllib.parse.urlparse(url).netloc
        expiration_date = cert['notAfter']

        # Add the domain and expiration date to the results dictionary
        results[domain] = expiration_date

    return results
myString = 'This is a test string with some URLs: https://www.example1.com, https://www.example2.com, http://www.example3.com, and https://www.example4.com.'