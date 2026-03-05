import xml.etree.ElementTree as ET
from xml.dom import minidom
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def verify_relayable_signature(public_key, doc, signature):
    """
    Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
    """
    key = RSA.import_key(public_key)
    hash_obj = SHA256.new()
    hash_obj.update(doc.encode('utf-8'))
    verifier = pkcs1_15.new(key)
    try:
        verifier.verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False