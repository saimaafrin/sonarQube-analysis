def identify_request(request: RequestType):
    try:
        json_body = request.json
        if 'events' in json_body:
            return True
    except Exception:
        pass

    try:
        xml_body = request.xml
        if xml_body.tag == Magic_ENV_TAG:
            return True
    except Exception:
        pass

    return False