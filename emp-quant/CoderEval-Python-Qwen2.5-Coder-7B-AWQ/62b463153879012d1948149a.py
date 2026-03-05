def _group_files_by_xml_filename(source, xmls, files):
    grouped_data = {}
    for file in files:
        for xml in xmls:
            if file.startswith(xml):
                if xml not in grouped_data:
                    grouped_data[xml] = []
                grouped_data[xml].append(file)
                break
    return grouped_data