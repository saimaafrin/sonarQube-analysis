def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not image_href:
		raise ValueError("Image href is empty")

	parsed_url = urlparse(image_href)
	if not parsed_url.scheme:
		raise ValueError("Image href is missing scheme")

	if parsed_url.scheme not in ("http", "https"):
		raise ValueError("Image href scheme is not http or https")

	if not parsed_url.netloc:
		raise ValueError("Image href is missing netloc")

	if not parsed_url.path:
		raise ValueError("Image href is missing path")

	if parsed_url.path.endswith("/"):
		raise ValueError("Image href path ends with a slash")

	if not parsed_url.query:
		raise ValueError("Image href is missing query")

	if not parsed_url.query.startswith("?"):
		raise ValueError("Image href query does not start with a question mark")

	if not parsed_url.fragment:
		raise ValueError("Image href is missing fragment")

	if not parsed_url.fragment.startswith("#"):
		raise ValueError("Image href fragment does not start with a hash")

	image_id = parsed_url.fragment[1:]
	if not image_id:
		raise ValueError("Image href fragment is empty")

	return image_id, parsed_url.netloc, parsed_url.scheme == "https"