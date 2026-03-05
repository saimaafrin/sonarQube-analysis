import sys
from configparser import ConfigParser
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'
def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Read the configuration file
    config = ConfigParser()
    config.read(config_file)

    # Update the configuration file
    config.set('section', 'option', 'value')
    with open(config_file, 'w') as f:
        config.write(f)

    # Return the updated configuration and the path to the configuration file
    return config, config_file