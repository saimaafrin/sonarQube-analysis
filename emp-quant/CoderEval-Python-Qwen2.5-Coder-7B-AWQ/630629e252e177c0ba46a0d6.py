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
        return etree.fromstring(response.content, etree.XMLParser(remove_comments=True))
    else:
        raise Exception(f"Failed to retrieve host-meta for {host}")