def base_config(user, etcd_host="localhost", etcd_port=2379):
# Create a dictionary to hold the configuration
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
			"path": "/api/docs"
		},
		"log": {
			"level": "info",
			"file": "/var/log/user.log"
		}
	}

	# Add user-specific information to the configuration
	config["user"] = user

	return config