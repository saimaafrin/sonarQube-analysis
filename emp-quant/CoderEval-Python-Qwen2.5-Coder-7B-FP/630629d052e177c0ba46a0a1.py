def verify_relayable_signature(public_key, doc, signature):
# Create a new document from the original one
	new_doc = etree.fromstring(etree.tostring(doc))
	
	# Remove all signature nodes from the new document
	signature_nodes = new_doc.xpath(".//ds:Signature", namespaces={"ds": "http://www.w3.org/2000/09/xmldsig#"})
	for node in signature_nodes:
		node.getparent().remove(node)
	
	# Sign the new document using the provided public key and signature
	signed_new_doc = sign_document(new_doc, public_key, signature)
	
	# Compare the original document with the signed new document
	if etree.tostring(doc) == etree.tostring(signed_new_doc):
		return True
	else:
		return False