from typing import List

class IniType:
    def __init__(self, file_names: List[str]):
        self.file_names = file_names

class cli:
    @staticmethod
    def ListOfFileNames(file_names: List[str]) -> IniType:
        return IniType(file_names)

def list_of_file_names(settings_dirs: List[str], spec_option: str) -> IniType:
    # Assuming settings_dirs is a list of directory paths and spec_option is a string
    # For demonstration purposes, let's assume we get the file names from these directories
    import os
    file_names = []
    for dir_path in settings_dirs:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if spec_option in file:
                    file_names.append(os.path.join(root, file))
    return cli.ListOfFileNames(file_names)