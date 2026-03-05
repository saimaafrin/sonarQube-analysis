import zipfile

def _explore_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        grouped_files = _group_files_by_xml_filename(file_list)
        return grouped_files

def _group_files_by_xml_filename(file_list):
    grouped = {}
    for file_name in file_list:
        if file_name.endswith('.xml'):
            base_name = file_name.rsplit('.', 1)[0]
            if base_name in grouped:
                grouped[base_name].append(file_name)
            else:
                grouped[base_name] = [file_name]
    return grouped