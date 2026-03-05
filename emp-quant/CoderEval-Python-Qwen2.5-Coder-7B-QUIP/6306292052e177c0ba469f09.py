def identify_request(request: RequestType):
    if request.body.is_json():
        return request.body.json().get('events', False)
    elif request.body.is_xml() and request.body.xml().tag == 'Magic_ENV_TAG':
        return True
    else:
        return False