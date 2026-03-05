def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	return {
		"tls": {
			"cert": "/etc/ssl/certs/etcd/server.crt",
			"key": "/etc/ssl/certs/etcd/server.key",
			"client_cert": "/etc/ssl/certs/etcd/client.crt",
			"client_key": "/etc/ssl/certs/etcd/client.key",
			"client_ca": "/etc/ssl/certs/etcd/client.crt",
			"client_auth": "false",
			"client_auth_fail_fast": "false",
			"client_auth_fail_fast_timeout": "10s",
			"client_cert_expiry": "12h",
			"client_cert_expiry_ca": "false",
			"client_cert_expiry_check_interval": "10s",
			"client_cert_expiry_check_timeout": "10s",
			"client_cert_expiry_check_timeout_start": "10s",
			"client_cert_expiry_check_timeout_args": "10s",
			"client_cert_expiry_check_timeout_args_start": "10s",
			"client_cert_expiry_check_timeout_args_args": "10s",
			"client_cert_expiry_check_timeout_args_args_args": "10s",
			"client_cert_expiry_check_timeout_args_args_args_args": "10s",
			"client_cert_expiry_check_timeout_args_args_args_args_args": "10s",
			"client_cert_expiry_check_timeout_args_args_args_args_args_args": "10s",
			"client_cert_expiry_check_timeout_args_args_args_args_args_args_args": "10s",
			"client_cert