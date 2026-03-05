import zipfile
import os

def _explore_zipfile(zip_path):
    """
    Groups the given zip path by using _group_files_by_xml_filename.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]
        non_xml_files = [file for file in zip_ref.namelist() if not file.endswith('.xml')]
        _group_files_by_xml_filename(xml_files, non_xml_files)

def _group_files_by_xml_filename(xml_files, non_xml_files):
    """
    Groups files by XML and non-XML files.
    """
    xml_dict = {}
    non_xml_dict = {}

    for xml_file in xml_files:
        xml_dict[xml_file] = [file for file in non_xml_files if file.startswith(xml_file.split('.')[0])]

    for non_xml_file in non_xml_files:
        non_xml_dict[non_xml_file] = [file for file in xml_files if file.startswith(non_xml_file.split('.')[0])]

    return xml_dict, non_xml_dict