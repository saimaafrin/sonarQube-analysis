def _replace_url_args(url, url_args):
    """
    Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
    """
    if url_args:
        url_parts = url.split('?')
        if len(url_parts) > 1:
            query_string = url_parts[1]
            query_params = query_string.split('&')
            for key, value in url_args.items():
                query_params = [param for param in query_params if not param.startswith(f'{key}={') or param.split('=')[1] != value]
                query_params.append(f'{key}={value}')
            url_parts[1] = '&'.join(query_params)
            url = '&'.join(url_parts)
    return url