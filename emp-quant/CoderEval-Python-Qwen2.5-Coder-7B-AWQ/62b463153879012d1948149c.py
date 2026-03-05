def select_filenames_by_prefix(prefix, files):
    return [file for file in files if file.startswith(prefix)]