import zipfile

def _explore_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        xml_files = [f for f in zip_ref.namelist() if f.endswith('.xml')]
        grouped_files = {}
        for file in xml_files:
            key = file.split('_')[0]  # Assuming the grouping is based on the part before the first underscore
            if key not in grouped_files:
                grouped_files[key] = []
            grouped_files[key].append(file)
        return grouped_files