import os

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"File {config_filename} already exists and overwrite is set to False.")
    
    with open(config_filename, 'w', mode=mode) as f:
        f.write(rendered_config)