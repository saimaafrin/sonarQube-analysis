def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
# Split the href by '/'
	parts = image_href.split('/')
	if len(parts) < 3:
		raise ValueError('Invalid image href')

	# Extract the image ID and netloc from the parts
	image_id = parts[-1]
	netloc_parts = parts[:-1]

	# Check if the href uses SSL
	use_ssl = False
	if netloc_parts[0] == 'https':
		use_ssl = True
		netloc_parts.pop(0)

	# Join the remaining parts to get the netloc
	netloc = '/'.join(netloc_parts)

	return image_id, netloc, use_ssl