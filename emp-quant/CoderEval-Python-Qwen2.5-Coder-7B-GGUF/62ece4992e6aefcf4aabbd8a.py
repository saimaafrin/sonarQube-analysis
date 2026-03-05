import os
import json
import logging

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    config_dict = {}
    error_logs = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                if resolve_env:
                    config = resolve_environment_variables(config)
                config_dict[filename] = config
        except (PermissionError, json.JSONDecodeError) as e:
            error_logs.append(logging.LogRecord('load_configurations', logging.ERROR, filename, None, str(e), None, None))

    if overrides:
        for key, value in overrides.items():
            if key in config_dict:
                config_dict[key].update(value)

    return config_dict, error_logs

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