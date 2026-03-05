def _group_files_by_xml_filename(source, xmls, files):
    """
    Groups files by xmls and returns data in dict format.
    """
    grouped_files = {}
    for xml in xmls:
        grouped_files[xml] = [file for file in files if file.startswith(xml)]
    return grouped_files