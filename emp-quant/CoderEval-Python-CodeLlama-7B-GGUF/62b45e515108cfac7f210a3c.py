def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self.logger.info("Initializing OCFL storage root")
	self.storage_root = self.config.get("storage_root")
	self.storage_root_path = Path(self.storage_root)
	self.storage_root_path.mkdir(parents=True, exist_ok=True)
	self.storage_root_path.chmod(0o755)
	self.storage_root_path.joinpath("config").mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath("config").chmod(0o755)
	self.storage_root_path.joinpath("content").mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath("content").chmod(0o755)
	self.storage_root_path.joinpath("version").mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath("version").chmod(0o755)
	self.storage_root_path.joinpath("version").joinpath("1.0").mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath("version").joinpath("1.0").chmod(0o755)
	self.storage_root_path.joinpath("version").joinpath("1.0").joinpath("content").mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath("version").joinpath("1.0").joinpath("content").chmod(0o755)
	self.storage_root_path.joinpath("version").joinpath("1.0").joinpath("version").mkdir(parents=True, exist_ok=True)
	self.storage_root_path.joinpath("version").joinpath("1.0").joinpath("version").chmod(0o755)
	self.storage_root_path.joinpath("version").joinpath("1.0").joinpath("version").joinpath("1").mkdir(parents=True