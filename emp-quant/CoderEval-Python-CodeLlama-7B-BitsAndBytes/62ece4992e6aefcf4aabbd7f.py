def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not image_href:
		raise ValueError("Image href cannot be empty")

	parsed_url = urlparse(image_href)
	if not parsed_url.netloc:
		raise ValueError("Image href must contain a netloc")

	if parsed_url.scheme not in ["http", "https"]:
		raise ValueError("Image href must have a valid scheme")

	return parsed_url.path, parsed_url.netloc, parsed_url.scheme == "https"