def _explore_folder(folder):
    """
    Groups files in the given group by using _group_files_by_xml_filename.
    """
    files = os.listdir(folder)
    grouped_files = _group_files_by_xml_filename(files)
    return grouped_files