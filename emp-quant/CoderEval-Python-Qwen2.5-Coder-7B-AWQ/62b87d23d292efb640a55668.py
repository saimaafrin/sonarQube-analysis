from versioneer import VersioneerConfig

def get_config():
    config = VersioneerConfig()
    config.versionfile_source = "src/my_package/_version.py"
    config.versionfile_build = "build/src/my_package/_version.py"
    config.tag_prefix = "v"
    config.parentdir_prefix = "my_package-"
    return config