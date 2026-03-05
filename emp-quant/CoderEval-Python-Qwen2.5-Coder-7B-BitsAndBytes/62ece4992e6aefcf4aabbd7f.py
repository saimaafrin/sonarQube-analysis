from typing import Tuple
import urllib.parse

def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    parsed_url = urllib.parse.urlparse(image_href)
    if not parsed_url.netloc:
        raise ValueError("Invalid image href")
    
    image_id = parsed_url.path.split('/')[-1]
    netloc = parsed_url.netloc
    use_ssl = parsed_url.scheme == 'https'
    
    return image_id, netloc, use_ssl