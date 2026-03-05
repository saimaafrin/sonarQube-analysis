import zipfile

def _explore_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        xml_files = [f for f in file_list if f.endswith('.xml')]
        grouped_files = {}
        for xml_file in xml_files:
            base_name = xml_file.split('.')[0]
            grouped_files[base_name] = [f for f in file_list if f.startswith(base_name)]
        return grouped_files