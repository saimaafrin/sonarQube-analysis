def _group_files_by_xml_filename(source, xmls, files):
    grouped_files = {}
    for xml in xmls:
        grouped_files[xml] = []
    for file in files:
        if file.endswith('.xml'):
            continue
        xml_name = source + '/' + file.split('.')[0] + '.xml'
        if xml_name in grouped_files:
            grouped_files[xml_name].append(file)
    return grouped_files