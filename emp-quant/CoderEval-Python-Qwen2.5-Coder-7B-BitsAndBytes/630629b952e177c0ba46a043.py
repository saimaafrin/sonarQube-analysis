import requests

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Returns a formatted dictionary, including information such as url and document_path.
    """
    if document_path is None:
        document_path = '/.well-known/nodeinfo'
    
    full_url = f"{url}{document_path}"
    response = requests.get(full_url)
    
    if response.status_code == 200:
        return {
            'url': full_url,
            'document_path': document_path,
            'content': response.json()
        }
    else:
        return {
            'url': full_url,
            'document_path': document_path,
            'status_code': response.status_code,
            'error': response.text
        }