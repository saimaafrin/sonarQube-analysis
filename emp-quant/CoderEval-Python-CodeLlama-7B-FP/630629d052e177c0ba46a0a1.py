def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	# Verify the signature
	try:
		public_key.verify(signature, doc)
	except Exception as e:
		print("Error verifying signature: %s" % e)
		return False
	return True