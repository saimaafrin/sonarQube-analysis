
import subprocess
import csv
import os

def task_func(commands_file_path, output_dir_path):
    # Check if the commands file exists
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"The file {commands_file_path} does not exist.")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    output_files = []
    
    # Read the commands from the CSV file
    with open(commands_file_path, mode='r') as file:
        reader = csv.reader(file)
        commands = [row[0] for row in reader]
    
    # Execute each command and save the output
    for index, command in enumerate(commands):
        output_file_path = os.path.join(output_dir_path, f'command_{index}_output.txt')
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            with open(output_file_path, 'wb') as output_file:
                output_file.write(result.stdout)
        except subprocess.CalledProcessError as e:
            with open(output_file_path, 'w') as output_file:
                output_file.write(f"Command failed with exit code {e.returncode}: {e.stderr.decode()}")
            raise Exception(f"Command '{command}' failed with exit code {e.returncode}.")
        
        output_files.append(output_file_path)
    
    return output_files