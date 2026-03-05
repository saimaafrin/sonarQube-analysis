import requests

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Returns a formatted dictionary, including information such as url and document_path.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if document_path:
            return {**data, 'url': url, 'document_path': document_path}
        else:
            return {**data, 'url': url}
    else:
        return {'error': 'Failed to retrieve document', 'url': url}