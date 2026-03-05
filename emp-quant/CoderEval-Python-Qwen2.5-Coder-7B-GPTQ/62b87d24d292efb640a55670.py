import pkg_resources

def get_versions():
    try:
        return pkg_resources.get_distribution('your_package_name').version
    except pkg_resources.DistributionNotFound:
        return 'default_version'