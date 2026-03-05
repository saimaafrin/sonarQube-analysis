
import subprocess
import csv
import os

def task_func(commands_file_path, output_dir_path):
    # Check if the commands file exists
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"The file {commands_file_path} does not exist.")

    # Ensure the output directory exists
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # List to hold the paths of the output files
    output_file_paths = []

    # Read commands from the CSV file
    with open(commands_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            command = row[0]
            output_file_path = os.path.join(output_dir_path, f'command_{index}_output.txt')

            # Execute the command and capture the output
            try:
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output_file_paths.append(output_file_path)
                with open(output_file_path, 'w') as output_file:
                    output_file.write(result.stdout.decode('utf-8'))
            except subprocess.CalledProcessError as e:
                output_file_paths.append(output_file_path)
                with open(output_file_path, 'w') as output_file:
                    output_file.write(f"Error: {e.stderr.decode('utf-8')}\nExit Code: {e.returncode}")

    return output_file_paths