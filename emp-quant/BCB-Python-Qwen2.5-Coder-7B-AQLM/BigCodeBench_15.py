
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
    
    # List to store the paths of the output files
    output_files = []
    
    # Read the commands from the CSV file
    with open(commands_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for index, command in enumerate(reader):
            command = command[0].strip()  # Assuming the command is in the first column
            output_file_path = os.path.join(output_dir_path, f'command_{index}_output.txt')
            output_files.append(output_file_path)
            
            # Execute the command
            try:
                result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                with open(output_file_path, 'w') as output_file:
                    output_file.write(result.stdout)
            except subprocess.CalledProcessError as e:
                with open(output_file_path, 'w') as output_file:
                    output_file.write(f"Error: {e.stderr}\nExit Code: {e.returncode}")
    
    return output_files