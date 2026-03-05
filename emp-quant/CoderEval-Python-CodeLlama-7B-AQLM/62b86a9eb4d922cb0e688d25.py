def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		"cluster": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"namespace": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"node": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"pod": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"service": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"ingress": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"deployment": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"statefulset": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"daemonset": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"job": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"cronjob": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"secret": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"configmap": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"persistentvolume": "^[a-z0-9]([-a-z0-9]*[a-z0-9])?$",
		"persistentvolumeclaim": "^[a-z0-9]([-a