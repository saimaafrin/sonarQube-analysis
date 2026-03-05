import requests
from lxml import etree

def retrieve_diaspora_host_meta(host):
    """
    Retrieve a remote Diaspora host-meta document.

    :arg host: Host to retrieve from
    :returns: ``XRD`` instance
    """
    url = f"https://{host}/host-meta"
    response = requests.get(url)
    if response.status_code == 200:
        xrd = etree.fromstring(response.content)
        return xrd
    else:
        raise Exception(f"Failed to retrieve host-meta document for {host}")