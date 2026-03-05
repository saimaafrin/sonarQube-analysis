def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	# Verify the signature
	try:
		verifier = XMLVerifier(public_key)
		verifier.verify(doc, signature)
	except Exception as e:
		print("Error verifying signature: " + str(e))
		return False
	return True