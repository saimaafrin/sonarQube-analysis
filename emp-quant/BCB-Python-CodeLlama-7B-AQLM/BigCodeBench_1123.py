import re
import urllib.parse
import ssl
import socket
def task_func(myString):
    """
    Extracts all URLs from a string and retrieves the domain and the expiration date of the SSL certificate 
    for each HTTPS URL. Only HTTPS URLs are processed; HTTP URLs are ignored. The function handles SSL errors 
    by ignoring any HTTPS URLs where the SSL certificate cannot be retrieved due to such errors, and these domains 
    are not included in the returned dictionary.

    Parameters:
    myString (str): The string from which to extract URLs.
    
    Returns:
    dict: A dictionary with domains as keys and SSL certificate expiry dates in UTC format as values. 
          The dictionary includes only those HTTPS URLs for which the SSL certificate was successfully retrieved.
          Domains with SSL errors are excluded.

    Requirements:
    - re
    - urllib.parse
    - ssl
    - socket
    
    Example:
    >>> task_func("Check these links: https://www.google.com, https://www.python.org")
    {'www.google.com': '2023-06-15 12:00:00', 'www.python.org': '2023-07-20 12:00:00'}
    """
    # Extract all URLs from the string
    urls = re.findall(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', myString)
    # Create an empty dictionary to store the results
    results = {}
    # Iterate over the URLs
    for url in urls:
        # Check if the URL is HTTPS
        if url.startswith('https://'):
            # Parse the URL
            parsed_url = urllib.parse.urlparse(url)
            # Extract the domain
            domain = parsed_url.netloc
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the domain
            try:
                sock.connect((domain, 443))
            except:
                # If the connection fails, ignore the URL
                continue
            # Create an SSL context
            context = ssl.create_default_context()
            # Retrieve the SSL certificate
            try:
                cert = context.wrap_socket(sock, server_hostname=domain)
                # Extract the expiration date of the certificate
                expiry_date = cert.getpeercert()['notAfter']
                # Convert the expiration date to UTC format
                expiry_date = expiry_date.decode('utf-8')
                expiry_date = expiry_date[:16] + ' UTC'
                # Add the domain and the expiration date to the results dictionary
                results[domain] = expiry_date
            except:
                # If the SSL certificate cannot be retrieved, ignore the URL
                continue
            # Close the socket
            sock.close()
    # Return the results dictionary
    return results