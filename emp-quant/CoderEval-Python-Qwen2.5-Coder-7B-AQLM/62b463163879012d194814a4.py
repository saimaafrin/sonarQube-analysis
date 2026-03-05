import zipfile

def _explore_zipfile(zip_path):
    """
    Groups the given zip path by using _group_files_by_xml_filename.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]
        grouped_files = _group_files_by_xml_filename(xml_files)
        return grouped_files

def _group_files_by_xml_filename(xml_files):
    """
    Groups files by their XML filename.
    """
    grouped_files = {}
    for xml_file in xml_files:
        base_name = xml_file.split('.')[0]
        if base_name not in grouped_files:
            grouped_files[base_name] = []
        grouped_files[base_name].append(xml_file)
    return grouped_files