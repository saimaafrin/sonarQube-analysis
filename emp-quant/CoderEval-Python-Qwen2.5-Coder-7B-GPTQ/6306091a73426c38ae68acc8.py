from typing import List

class IniType:
    pass

class cli:
    @staticmethod
    def ListOfFileNames() -> IniType:
        return IniType()

def list_of_file_names(settings_dirs: List[str], spec_option: str) -> IniType:
    """
    Create and return a new IniType complex type via cli.ListOfFileNames()
    """
    return cli.ListOfFileNames()