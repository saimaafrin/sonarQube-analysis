def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
# Importing necessary libraries
	import subprocess

	# Check if commands is a single string or a list
	if isinstance(commands, str):
		commands = [commands]

	# Initialize an empty list to store results
	results = []

	# Loop through each command
	for cmd in commands:
		# Construct the full command with arguments
		full_cmd = [cmd] + args

		# Set up the subprocess call
		process = subprocess.Popen(full_cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)

		# Wait for the process to complete and capture output
		stdout, stderr = process.communicate()

		# If verbose mode is on, print the command and its output
		if verbose:
			print(f"Command: {' '.join(full_cmd)}")
			print("Output:")
			print(stdout.decode())
			if not hide_stderr:
				print("Error Output:")
				print(stderr.decode())

		# Append the result as a tuple (stdout, stderr, returncode) to the results list
		results.append((stdout, stderr, process.returncode))

	# Return all results
	return results