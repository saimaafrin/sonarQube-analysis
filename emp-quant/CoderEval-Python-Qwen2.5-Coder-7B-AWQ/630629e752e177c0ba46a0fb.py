import requests

def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    """
    Send a response containing data through the POST method.
    """
    if method.lower() == "post":
        return requests.post(url, data=data, timeout=timeout, *args, **kwargs)
    else:
        raise ValueError("Unsupported method")