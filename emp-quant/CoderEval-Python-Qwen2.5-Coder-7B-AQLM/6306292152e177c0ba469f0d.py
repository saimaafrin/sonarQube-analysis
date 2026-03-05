import json

def identify_request(request: RequestType) -> bool:
    try:
        body = json.loads(request.body)
        return 'events' in body
    except json.JSONDecodeError:
        return False