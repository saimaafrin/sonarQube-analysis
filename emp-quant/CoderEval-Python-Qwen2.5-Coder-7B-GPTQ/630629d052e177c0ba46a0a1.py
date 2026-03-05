from lxml import etree
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def verify_relayable_signature(public_key, doc, signature):
    try:
        # Parse the document and extract the signed element
        root = etree.fromstring(doc)
        signed_element = root.find('.//{http://www.w3.org/2000/09/xmldsig#}Signature')
        
        # Extract the digest value from the signature
        digest_value = signed_element.find('.//{http://www.w3.org/2000/09/xmldsig#}DigestValue').text
        
        # Calculate the digest of the signed element
        canonicalized_data = etree.tostring(signed_element, pretty_print=True).decode('utf-8')
        digest = hashlib.sha256(canonicalized_data.encode('utf-8')).digest()
        
        # Verify the signature using the public key
        public_key.verify(
            base64.b64decode(signature),
            digest,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False