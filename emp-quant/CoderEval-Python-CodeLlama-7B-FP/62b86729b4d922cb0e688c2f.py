def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"tls": {
			"enabled": False,
			"cert": None,
			"key": None,
			"ca": None
		},
		"authentication": {
			"enabled": False,
			"username": None,
			"password": None
		},
		"authorization": {
			"enabled": False,
			"roles": []
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port,
			"prefix": "/"
		},
		"docs": {
			"enabled": False,
			"path": None
		},
		"log": {
			"level": "info",
			"path": None
		}
	}
	if user is not None:
		config["authentication"]["username"] = user
	return config