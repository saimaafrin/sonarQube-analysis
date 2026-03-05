def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not image_href:
		raise ValueError("Image href is empty")

	image_id = None
	netloc = None
	use_ssl = False

	if image_href.startswith("http://"):
		netloc = image_href[7:]
		use_ssl = False
	elif image_href.startswith("https://"):
		netloc = image_href[8:]
		use_ssl = True
	else:
		raise ValueError("Image href is not a valid URL")

	if "/" in netloc:
		image_id = netloc.split("/")[0]
		netloc = netloc.split("/")[1]

	return image_id, netloc, use_ssl