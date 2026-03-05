import subprocess
import csv
import os
def task_func(commands_file_path, output_dir_path):
    """
    Execute a list of shell commands read from a CSV file and save the outputs in separate files.
    Each command's output is written to a unique file in the specified output directory.
    If a command fails, the error message along with the exit code is appended to the respective output file.
    """
    # Check if the commands file exists
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"The commands file {commands_file_path} does not exist.")

    # Create the output directory if it does not exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Read the commands from the CSV file
    with open(commands_file_path, "r") as f:
        reader = csv.reader(f)
        commands = [row[0] for row in reader]

    # Execute each command and save the output to a file
    output_files = []
    for i, command in enumerate(commands):
        try:
            # Execute the command and save the output to a file
            output = subprocess.check_output(command, shell=True)
            output_file_path = os.path.join(output_dir_path, f"command_{i}_output.txt")
            with open(output_file_path, "w") as f:
                f.write(output.decode("utf-8"))
            output_files.append(output_file_path)
        except subprocess.CalledProcessError as e:
            # If the command fails, append the error message and exit code to the output file
            output_file_path = os.path.join(output_dir_path, f"command_{i}_output.txt")
            with open(output_file_path, "a") as f:
                f.write(f"Error: {e.output.decode('utf-8')}\nExit code: {e.returncode}")
            output_files.append(output_file_path)

    return output_files