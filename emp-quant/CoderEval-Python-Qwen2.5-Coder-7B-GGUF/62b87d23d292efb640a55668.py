from versioneer import VersioneerConfig

def get_config():
    config = VersioneerConfig(
        version_scheme="pep440",
        parentdir_prefix="mypackage-",
        versionfile_source="mypackage/_version.py",
        versionfile_build="mypackage/_version.py",
        tag_prefix="v",
        parentdir_prefix_re=None,
        versionfile_source_re=None,
        versionfile_build_re=None,
        verbose=True,
    )
    return config