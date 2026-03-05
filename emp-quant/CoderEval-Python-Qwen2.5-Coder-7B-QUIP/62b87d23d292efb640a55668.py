from versioneer import VersioneerConfig

def get_config():
    config = VersioneerConfig()
    config.command_default = 'pyproject.toml'
    config.command_options = {
        'build': {
            'pyproject.toml': 'build',
            'setup.py': 'build',
        },
        'install': {
            'pyproject.toml': 'install',
            'setup.py': 'install',
        },
        'develop': {
            'pyproject.toml': 'develop',
            'setup.py': 'develop',
        },
        'uninstall': {
            'pyproject.toml': 'uninstall',
            'setup.py': 'uninstall',
        },
        'sdist': {
            'pyproject.toml': 'sdist',
            'setup.py': 'sdist',
        },
        'bdist': {
            'pyproject.toml': 'bdist',
            'setup.py': 'bdist',
        },
        'check': {
            'pyproject.toml': 'check',
            'setup.py': 'check',
        },
        'test': {
            'pyproject.toml': 'test',
            'setup.py': 'test',
        },
    }
    config.package_name = 'example_package'
    config.package_version = '0.1.0'
    config.package_author = 'John Doe'
    config.package_email = 'john.doe@example.com'
    config.package_description = 'A sample package for Versioneer'
    config.package_long_description = 'A sample package for Versioneer'
    config.package_url = 'https://example.com'
    config.package_license = 'MIT'
    config.package_classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
    config.package_python_requires = '>=3.6'
    config.package_extras_require = {
        'dev': ['pytest'],
    }
    config.package_data = {
        '': ['*.txt', '*.rst'],
    }
    config.package_package_dir = {
        '': 'src',
    }
    config.package_package_data = {
        '': ['*.txt', '*.rst'],
    }
    config.package_package_dir = {
        '': 'src',
    }
    config.package_package_data = {
        '': ['*.txt', '*.rst'],
    }
    config.package_package_dir = {
        '': 'src