
import subprocess
import csv
import os

def task_func(commands_file_path, output_dir_path):
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"File {commands_file_path} does not exist.")

    with open(commands_file_path, "r") as f:
        reader = csv.reader(f)
        commands = [row[0] for row in reader]

    output_files = []
    for i, command in enumerate(commands):
        output_file = os.path.join(output_dir_path, f"command_{i}_output.txt")
        try:
            with open(output_file, "w") as f:
                subprocess.run(command, stdout=f, stderr=subprocess.PIPE, check=False)
        except subprocess.CalledProcessError as e:
            with open(output_file, "a") as f:
                f.write(f"Command {i} failed with exit code {e.returncode}\n")
                f.write(e.output.decode("utf-8"))
        output_files.append(output_file)

    return output_files