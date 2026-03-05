import os
import logging
from typing import List, Tuple, Dict, Optional

def load_configurations(config_filenames: List[str], overrides: Optional[Dict[str, any]] = None, resolve_env: bool = True) -> Tuple[Dict[str, any], List[logging.LogRecord]]:
    config_dict = {}
    error_log = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = file.read()
                config_dict[filename] = config
        except (IOError, SyntaxError) as e:
            error_log.append(logging.LogRecord('error', e.args[0], e.filename, e.lineno, e.offset, e.msg, e.args))

    if overrides:
        for key, value in overrides.items():
            if key in config_dict:
                config_dict[key] = value

    if resolve_env:
        for key, value in config_dict.items():
            if isinstance(value, str):
                config_dict[key] = os.environ.get(value, value)

    return config_dict, error_log