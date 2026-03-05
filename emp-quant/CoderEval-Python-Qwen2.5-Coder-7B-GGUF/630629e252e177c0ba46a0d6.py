import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    url = f"https://{host}/.well-known/host-meta"
    response = requests.get(url)
    if response.status_code == 200:
        xrd_content = response.text
        xrd_root = etree.fromstring(xrd_content, etree.XMLParser(ns_clean=True))
        return xrd_root
    else:
        raise Exception(f"Failed to retrieve host-meta document from {host}")