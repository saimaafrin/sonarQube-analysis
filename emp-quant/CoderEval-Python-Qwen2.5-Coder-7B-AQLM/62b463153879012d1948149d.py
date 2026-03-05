import os

def _explore_folder(folder):
    """
    Groups files in the given group by using _group_files_by_xml_filename.
    """
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    grouped_files = _group_files_by_xml_filename(files)
    return grouped_files

def _group_files_by_xml_filename(files):
    """
    Groups files based on their XML filename.
    """
    grouped = {}
    for file in files:
        if file.endswith('.xml'):
            key = file.split('.')[0]
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(file)
    return grouped