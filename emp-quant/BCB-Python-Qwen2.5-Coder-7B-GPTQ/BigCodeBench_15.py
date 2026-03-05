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

    # List to store the paths of output files
    output_files = []

    # Read the commands from the CSV file
    with open(commands_file_path, mode='r') as file:
        reader = csv.reader(file)
        for index, command in enumerate(reader):
            # Construct the output file path
            output_file_path = os.path.join(output_dir_path, f'command_{index}_output.txt')
            output_files.append(output_file_path)

            # Execute the command
            try:
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # Write the output to the file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(result.stdout.decode('utf-8'))
            except subprocess.CalledProcessError as e:
                # Write the error message and exit code to the file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(f"Error: {e.stderr.decode('utf-8')}\nExit Code: {e.returncode}")

    return output_files