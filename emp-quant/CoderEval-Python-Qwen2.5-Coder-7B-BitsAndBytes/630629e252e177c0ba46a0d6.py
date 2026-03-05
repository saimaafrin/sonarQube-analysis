import requests
from lxml import etree

class XRD:
    def __init__(self, data):
        self.data = data

def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    if response.status_code == 200:
        xrd_data = response.content
        return XRD(etree.fromstring(xrd_data))
    else:
        raise Exception(f"Failed to retrieve host-meta for {host}")