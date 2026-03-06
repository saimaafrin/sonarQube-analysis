def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if image_href.startswith("http://"):
		netloc = image_href[7:]
		use_ssl = False
	elif image_href.startswith("https://"):
		netloc = image_href[8:]
		use_ssl = True
	else:
		raise ValueError("Invalid image href: %s" % image_href)

	if ":" in netloc:
		image_id, netloc = netloc.split(":", 1)
	else:
		image_id = None

	return image_id, netloc, use_ssl