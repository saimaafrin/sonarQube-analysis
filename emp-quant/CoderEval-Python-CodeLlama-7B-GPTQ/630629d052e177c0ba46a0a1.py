def verify_relayable_signature(public_key, doc, signature):
	"""
	Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.
	"""
	# Verify the signature
	if not public_key.verify(doc.encode('utf-8'), signature):
		raise ValueError("Invalid signature")

	# Verify the timestamp
	timestamp = doc.find('./ns:Timestamp', NAMESPACES).text
	if not timestamp:
		raise ValueError("Missing timestamp")
	try:
		timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
	except ValueError:
		raise ValueError("Invalid timestamp")
	if abs(timestamp - datetime.utcnow()) > timedelta(minutes=5):
		raise ValueError("Timestamp too old")

	# Verify the nonce
	nonce = doc.find('./ns:Nonce', NAMESPACES).text
	if not nonce:
		raise ValueError("Missing nonce")
	if len(nonce) != 32:
		raise ValueError("Invalid nonce")
	if not re.match(r'[0-9a-f]+', nonce):
		raise ValueError("Invalid nonce")

	# Verify the signature algorithm
	signature_algorithm = doc.find('./ns:SignatureMethod', NAMESPACES).text
	if not signature_algorithm:
		raise ValueError("Missing signature algorithm")
	if signature_algorithm not in SIGNATURE_ALGORITHMS:
		raise ValueError("Invalid signature algorithm")

	# Verify the digest algorithm
	digest_algorithm = doc.find('./ns:DigestMethod', NAMESPACES).text
	if not digest_algorithm:
		raise ValueError("Missing digest algorithm")
	if digest_algorithm not in DIGEST_ALGORITHMS:
		raise ValueError("Invalid digest algorithm")

	# Verify the relay state
	relay_state = doc.find('./ns:RelayState', NAMESPACES).text
	if not relay_state:
		raise ValueError("Missing relay state")
	if len(relay_state) > 1024:
		raise Value