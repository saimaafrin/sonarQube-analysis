import os

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if os.path.exists(config_filename) and not overwrite:
        raise FileExistsError(f"The file {config_filename} already exists and overwrite is set to False.")
    
    with open(config_filename, 'w', mode=mode) as file:
        file.write(rendered_config)