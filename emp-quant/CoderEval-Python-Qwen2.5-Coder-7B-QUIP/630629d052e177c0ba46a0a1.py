import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

def verify_relayable_signature(public_key, doc, signature):
    # Load the public key
    key = RSA.import_key(public_key)

    # Parse the XML document
    root = ET.fromstring(doc)

    # Extract the signature from the XML
    signature = base64.b64decode(signature)

    # Create a SHA-256 hash of the document
    digest = SHA256.new(doc.encode())

    # Verify the signature
    verifier = PKCS1_v1_5.new(key)
    is_valid = verifier.verify(digest, signature, RSA.SHA256)

    return is_valid