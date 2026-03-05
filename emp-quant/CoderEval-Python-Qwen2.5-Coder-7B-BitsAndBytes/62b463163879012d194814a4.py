import zipfile

def _explore_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        grouped_files = {}
        for file in file_list:
            if file.endswith('.xml'):
                xml_name = file.split('.')[0]
                if xml_name not in grouped_files:
                    grouped_files[xml_name] = []
                grouped_files[xml_name].append(file)
        return grouped_files