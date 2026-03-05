from lxml import etree
from xmlsec import sign, crypto

def verify_relayable_signature(public_key, doc, signature):
    try:
        # Parse the XML document
        xml_doc = etree.fromstring(doc)
        
        # Load the public key
        pub_key = crypto.load_public_key(crypto.FILETYPE_PEM, public_key)
        
        # Verify the signature
        if sign.verify(xml_doc, signature, pub_key):
            return True
        else:
            return False
    except Exception as e:
        return False