def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"tls": {
			"cert": "/etc/ssl/certs/ssl-cert-snakeoil.pem",
			"key": "/etc/ssl/private/ssl-cert-snakeoil.key",
			"ca": "/etc/ssl/certs/ca-certificates.crt"
		},
		"authentication": {
			"type": "basic",
			"realm": "Authentication Realm",
			"users": {
				user: "password"
			}
		},
		"authorization": {
			"type": "basic",
			"realm": "Authorization Realm",
			"roles": {
				"admin": "admin",
				"user": "user"
			}
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"docs": {
			"path": "/docs"
		},
		"log": {
			"path": "/var/log/snakepit.log"
		}
	}
	return config