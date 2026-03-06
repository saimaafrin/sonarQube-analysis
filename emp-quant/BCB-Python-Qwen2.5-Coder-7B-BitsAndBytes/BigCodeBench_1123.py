
import re
import urllib.parse
import ssl
import socket

def get_ssl_expiry(url):
    try:
        hostname = urllib.parse.urlparse(url).hostname
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry_date = cert['notAfter']
                return expiry_date
    except Exception as e:
        print(f"SSL error for {url}: {e}")
        return None

def task_func(myString):
    url_pattern = re.compile(r'https://[^\s]+')
    urls = url_pattern.findall(myString)
    ssl_info_dict = {}
    
    for url in urls:
        expiry_date = get_ssl_expiry(url)
        if expiry_date:
            domain = urllib.parse.urlparse(url).netloc
            ssl_info_dict[domain] = expiry_date
    
    return ssl_info_dict