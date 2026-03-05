
import sys
from configparser import ConfigParser
# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'
def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Load the configuration file
    config = ConfigParser()
    config.read(config_file)

    # Update the configuration with the new path
    config['DEFAULT']['NEW_PATH'] = path_to_append

    # Write the updated configuration back to the file
    with open(config_file, 'w') as configfile:
        config.write(configfile)

    # Return the updated configuration and the path to the configuration file
    return config, config_file