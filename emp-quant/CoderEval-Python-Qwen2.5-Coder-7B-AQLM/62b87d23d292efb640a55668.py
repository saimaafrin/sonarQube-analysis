from versioneer import VersioneerConfig

def get_config():
    config = VersioneerConfig()
    config.VCS = 'git'
    config.versionfile_source = 'setup.py'
    config.versionfile_build = 'src/my_package/_version.py'
    config.tag_prefix = 'v'
    config.parentdir_prefix = 'my_package-'
    return config