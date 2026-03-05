from urllib.parse import urlparse, parse_qs, urlencode

def _replace_url_args(url, url_args):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    for key, value in url_args.items():
        if key in query_params:
            query_params[key] = [value]
    
    new_query_string = urlencode(query_params, doseq=True)
    modified_url = parsed_url._replace(query=new_query_string).geturl()
    
    return modified_url