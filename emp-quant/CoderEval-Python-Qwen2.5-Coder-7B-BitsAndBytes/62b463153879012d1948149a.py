from collections import defaultdict

def _group_files_by_xml_filename(source, xmls, files):
    grouped_files = defaultdict(list)
    
    for file in files:
        if file.endswith('.xml'):
            xml_name = file.replace('.xml', '')
            if xml_name in xmls:
                grouped_files[xml_name].append(file)
    
    return dict(grouped_files)