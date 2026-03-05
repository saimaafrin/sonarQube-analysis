import json
from xml.etree import ElementTree as ET

def identify_request(request: RequestType) -> bool:
    try:
        # Attempt to parse JSON
        data = json.loads(request.body)
        if 'events' in data:
            return True
    except json.JSONDecodeError:
        pass
    
    try:
        # Attempt to parse XML
        root = ET.fromstring(request.body)
        if root.tag == Magic_ENV_TAG:
            return True
    except ET.ParseError:
        pass
    
    return False