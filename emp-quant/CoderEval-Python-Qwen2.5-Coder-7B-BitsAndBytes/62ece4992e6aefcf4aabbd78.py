import socket

def is_local(host):
    """
    Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
    """
    local_ips = ['127.0.0.1', 'localhost']
    try:
        local_ips.extend(socket.gethostbyname_ex(socket.gethostname())[2])
    except socket.gaierror:
        pass
    return host in local_ips