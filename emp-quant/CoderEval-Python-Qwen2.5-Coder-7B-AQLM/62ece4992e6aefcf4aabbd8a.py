import os
import json
import logging

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    configurations = {}
    log_records = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                if resolve_env:
                    config = resolve_environment_variables(config)
                configurations[filename] = config
        except (FileNotFoundError, PermissionError) as e:
            logger.error(f"Error reading configuration file {filename}: {e}")
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing configuration file {filename}: {e}")
            log_records.append(logging.LogRecord(name=__name__, level=logging.ERROR, pathname=filename, lineno=0, msg=str(e), args=(), exc_info=None))

    if overrides:
        for filename, override in overrides.items():
            if filename in configurations:
                configurations[filename].update(override)

    return configurations, log_records

def resolve_environment_variables(config):
    for key, value in config.items():
        if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
            env_var = value[2:-1]
            if env_var in os.environ:
                config[key] = os.environ[env_var]
            else:
                config[key] = value
        elif isinstance(value, dict):
            config[key] = resolve_environment_variables(value)
        elif isinstance(value, list):
            config[key] = [resolve_environment_variables(item) if isinstance(item, dict) else item for item in value]
    return config