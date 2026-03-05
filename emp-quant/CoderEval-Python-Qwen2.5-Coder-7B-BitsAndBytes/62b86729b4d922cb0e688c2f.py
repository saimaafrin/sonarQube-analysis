def base_config(user, etcd_host="localhost", etcd_port=2379):
    config = {
        "tls": False,
        "authentication": True,
        "authorization": True,
        "etcd": {
            "host": etcd_host,
            "port": etcd_port
        },
        "docs": "path/to/docs",
        "log": {
            "level": "info",
            "file": "/var/log/app.log"
        }
    }
    return config