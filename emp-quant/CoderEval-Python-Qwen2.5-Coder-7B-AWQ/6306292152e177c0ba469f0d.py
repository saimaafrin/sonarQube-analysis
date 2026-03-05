import json

def identify_request(request: RequestType) -> bool:
    try:
        data = json.loads(request.body)
        return 'events' in data
    except json.JSONDecodeError:
        return False