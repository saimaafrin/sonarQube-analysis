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
        raise FileNotFoundError(f"The commands file '{commands_file_path}' does not exist.")

    # Create the output directory if it does not exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Read the commands from the CSV file
    with open(commands_file_path, "r") as f:
        reader = csv.reader(f)
        commands = [row for row in reader]

    # Execute the commands and save the outputs
    output_files = []
    for i, command in enumerate(commands):
        command_output_file = os.path.join(output_dir_path, f"command_{i}_output.txt")
        try:
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            with open(command_output_file, "w") as f:
                f.write("Command executed successfully.")
        except subprocess.CalledProcessError as e:
            with open(command_output_file, "a") as f:
                f.write(f"Command failed with exit code {e.returncode}.\n{e.output}")
        output_files.append(command_output_file)

    return output_files