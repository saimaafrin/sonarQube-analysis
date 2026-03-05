
import sys
from configparser import ConfigParser
# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'
def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    # Add the path to sys.path
    sys.path.append(path_to_append)
    # Load the configuration file
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    # Update the configuration file with the new path
    config.set('DEFAULT', 'path', path_to_append)
    # Save the updated configuration file
    with open(config_file, 'w') as config_file_handle:
        config.write(config_file_handle)
    return config, config_file