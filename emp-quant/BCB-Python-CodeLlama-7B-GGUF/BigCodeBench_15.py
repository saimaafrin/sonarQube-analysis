
import subprocess
import csv
import os

def task_func(commands_file_path, output_dir_path):
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"File not found: {commands_file_path}")

    with open(commands_file_path, 'r') as f:
        reader = csv.reader(f)
        commands = [row[0] for row in reader]

    output_files = []
    for i, command in enumerate(commands):
        output_file_path = os.path.join(output_dir_path, f"command_{i}_output.txt")
        try:
            subprocess.run(command, shell=True, check=True, stdout=open(output_file_path, 'w'))
        except subprocess.CalledProcessError as e:
            with open(output_file_path, 'a') as f:
                f.write(f"Error: {e.stderr.decode()}\nExit code: {e.returncode}")
        output_files.append(output_file_path)

    return output_files