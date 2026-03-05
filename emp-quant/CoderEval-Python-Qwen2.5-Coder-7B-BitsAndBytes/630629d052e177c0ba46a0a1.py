import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
    author did actually generate this message.
    """
    root = ET.fromstring(doc)
    for elem in root.iter():
        if 'Signature' in elem.tag:
            continue
        data = ET.tostring(elem, encoding='unicode')
        try:
            public_key.verify(
                base64.b64decode(signature),
                data.encode('utf-8'),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except Exception as e:
            return False
    return True