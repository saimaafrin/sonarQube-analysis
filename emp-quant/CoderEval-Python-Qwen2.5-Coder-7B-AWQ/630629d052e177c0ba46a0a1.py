from lxml import etree
from xmlsec import sign

def verify_relayable_signature(public_key, doc, signature):
    try:
        # Parse the document and signature
        doc_tree = etree.fromstring(doc)
        sig_tree = etree.fromstring(signature)

        # Load the public key
        key = sign.load_key_from_memory(public_key, format=sign.KeyFormat.PEM)

        # Verify the signature
        if sign.verify(sig_tree, key):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error verifying signature: {e}")
        return False