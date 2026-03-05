def _group_files_by_xml_filename(source, xmls, files):
    """
    Groups files by xmls and returns data in dict format.
    """
    grouped_files = {}
    for xml in xmls:
        grouped_files[xml] = []
    for file in files:
        if file.endswith('.xml'):
            xml_name = file.split('.')[0]
            if xml_name in grouped_files:
                grouped_files[xml_name].append(file)
    return grouped_files