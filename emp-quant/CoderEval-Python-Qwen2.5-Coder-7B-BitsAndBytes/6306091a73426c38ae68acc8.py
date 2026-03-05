from cli import ListOfFileNames

def list_of_file_names(settings_dirs, spec_option):
    """
    Create and return a new IniType complex type via cli.ListOfFileNames()
    """
    return ListOfFileNames(settings_dirs=settings_dirs, spec_option=spec_option)