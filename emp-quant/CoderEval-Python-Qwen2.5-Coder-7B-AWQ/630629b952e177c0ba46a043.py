import requests

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Returns a formatted dictionary, including information such as url and document_path.
    """
    if document_path:
        full_url = f"{url}/{document_path}"
    else:
        full_url = url
    
    response = requests.get(full_url)
    
    if response.status_code == 200:
        return {
            "url": full_url,
            "document_path": document_path,
            "content": response.text
        }
    else:
        return {
            "url": full_url,
            "document_path": document_path,
            "error": f"Failed to retrieve document. Status code: {response.status_code}"
        }