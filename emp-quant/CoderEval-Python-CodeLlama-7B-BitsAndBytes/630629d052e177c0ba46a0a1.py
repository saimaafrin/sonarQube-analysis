def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	# Verify the signature
	if not verify_signature(public_key, doc, signature):
		raise Exception("Signature verification failed")

	# Verify the timestamp
	if not verify_timestamp(doc):
		raise Exception("Timestamp verification failed")

	# Verify the nonce
	if not verify_nonce(doc):
		raise Exception("Nonce verification failed")

	# Verify the relay state
	if not verify_relay_state(doc):
		raise Exception("Relay state verification failed")

	# Verify the destination
	if not verify_destination(doc):
		raise Exception("Destination verification failed")

	# Verify the issuer
	if not verify_issuer(doc):
		raise Exception("Issuer verification failed")

	# Verify the audience
	if not verify_audience(doc):
		raise Exception("Audience verification failed")

	# Verify the subject
	if not verify_subject(doc):
		raise Exception("Subject verification failed")

	# Verify the message
	if not verify_message(doc):
		raise Exception("Message verification failed")

	# Verify the signature algorithm
	if not verify_signature_algorithm(doc):
		raise Exception("Signature algorithm verification failed")

	# Verify the digest algorithm
	if not verify_digest_algorithm(doc):
		raise Exception("Digest algorithm verification failed")

	# Verify the canonicalization method
	if not verify_canonicalization_method(doc):
		raise Exception("Canonicalization method verification failed")

	# Verify the reference URI
	if not verify_reference_uri(doc):
		raise Exception("Reference URI verification failed")

	# Verify the reference digest value
	if not verify_reference_digest_value(doc):
		raise Exception("Reference digest value verification failed")

	# Verify the reference digest method
	if not verify_reference_digest_method(doc):
		raise Exception("Reference digest method verification failed")

	# Ver