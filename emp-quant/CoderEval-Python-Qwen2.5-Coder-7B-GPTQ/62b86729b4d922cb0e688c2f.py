def base_config(user, etcd_host="localhost", etcd_port=2379):
    config = {
        "tls": False,
        "authentication": True,
        "authorization": True,
        "etcd": {
            "host": etcd_host,
            "port": etcd_port
        },
        "docs": {
            "enabled": True,
            "path": "/docs"
        },
        "log": {
            "level": "INFO",
            "file": "/var/log/app.log"
        }
    }
    return config