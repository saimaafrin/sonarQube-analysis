def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self.storage_root = self.config.get('storage_root')
	self.storage_root_id = self.config.get('storage_root_id')
	self.storage_root_path = os.path.join(self.storage_root, self.storage_root_id)
	self.storage_root_path_id = os.path.join(self.storage_root_path, self.storage_root_id)
	self.storage_root_path_objects = os.path.join(self.storage_root_path, 'objects')
	self.storage_root_path_versions = os.path.join(self.storage_root_path, 'versions')
	self.storage_root_path_version_map = os.path.join(self.storage_root_path, 'version-map')
	self.storage_root_path_version_map_json = os.path.join(self.storage_root_path_version_map, 'version-map.json')
	self.storage_root_path_version_map_txt = os.path.join(self.storage_root_path_version_map, 'version-map.txt')
	self.storage_root_path_version_map_md = os.path.join(self.storage_root_path_version_map, 'version-map.md')
	self.storage_root_path_version_map_html = os.path.join(self.storage_root_path_version_map, 'version-map.html')
	self.storage_root_path_version_map_xml = os.path.join(self.storage_root_path_version_map, 'version-map.xml')
	self.storage_root_path_version_map_yaml = os.path.join(self.storage_root_path_version_map, 'version-map.yaml')
	self.storage_root_path_version_map_yml = os.path.join(self.storage_root_path_version_map, 'version-map.yml')
	self.storage_root_path_version_map_properties = os.path.join(self.storage_root_path_version_