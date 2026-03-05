def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if image_href is None:
		raise ValueError("image_href must be a string")
	image_id = image_href.split("/")[-1]
	netloc = image_href.split("://")[1].split("/")[0]
	use_ssl = image_href.startswith("https")
	return image_id, netloc, use_ssl