import requests

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Returns a formatted dictionary, including information such as url and document_path.
    """
    response = requests.get(url)
    if response.status_code == 200:
        document_path = document_path or url.split('/')[-1]
        return {
            'url': url,
            'document_path': document_path,
            'content': response.text
        }
    else:
        return {
            'url': url,
            'document_path': None,
            'error': f'Failed to retrieve document. Status code: {response.status_code}'
        }