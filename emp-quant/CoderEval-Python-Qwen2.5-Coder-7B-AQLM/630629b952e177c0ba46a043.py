import requests

def get_nodeinfo_well_known_document(url, document_path=None):
    """
    Returns a formatted dictionary, including information such as url and document_path.
    """
    response = requests.get(url)
    if response.status_code == 200:
        document = response.json()
        if document_path:
            return {**document, "document_path": document_path}
        else:
            return document
    else:
        return {"error": "Failed to retrieve document", "status_code": response.status_code}