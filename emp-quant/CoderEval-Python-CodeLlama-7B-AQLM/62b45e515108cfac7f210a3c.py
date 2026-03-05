def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self.storage_root = self.storage_root_path
	self.storage_root_path.mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath('config.json').write_text(json.dumps(self.config))
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config.json').touch()
	self.storage_root_path.joinpath('config.json').chmod(0o644)
	self.storage_root_path.joinpath('config