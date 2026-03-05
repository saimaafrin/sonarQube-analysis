def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"tls": {
			"enabled": False,
			"cert": "",
			"key": "",
			"ca": ""
		},
		"authentication": {
			"enabled": False,
			"type": "basic",
			"username": "",
			"password": ""
		},
		"authorization": {
			"enabled": False,
			"type": "basic",
			"username": "",
			"password": ""
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port,
			"prefix": "config",
			"timeout": 10
		},
		"docs": {
			"enabled": False,
			"path": "docs"
		},
		"log": {
			"level": "info",
			"path": "logs"
		}
	}
	return config