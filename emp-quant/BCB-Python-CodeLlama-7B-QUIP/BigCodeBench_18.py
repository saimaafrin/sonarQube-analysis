
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    if not os.path.exists(file):
        return []
    if not file.endswith('.csv'):
        return []
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            lines = [line for line in reader]
    except Exception as e:
        return []
    if not lines:
        return []
    random.shuffle(lines)
    with open(file + '.split', 'w') as f:
        writer = csv.writer(f)
        for line in lines:
            writer.writerow(line)
    return [file + '.split']

def split_file(file):
    return [file + '.split']

def split_files(files):
    return [split_file(file) for file in files]

def split_file_list(files):
    return [split_file(file) for file in files]

def split_files_list(files):
    return [split_file(file) for file in files]

def split_file_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]

def split_files_list_list(files):
    return [split_file(file) for file in files]