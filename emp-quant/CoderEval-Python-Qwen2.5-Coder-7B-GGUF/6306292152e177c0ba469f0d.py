def identify_request(request: RequestType) -> bool:
    try:
        data = request.json
        return 'events' in data
    except ValueError:
        return False