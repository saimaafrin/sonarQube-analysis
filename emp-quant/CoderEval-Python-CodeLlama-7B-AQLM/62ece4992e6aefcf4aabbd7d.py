def subprocess_run_helper(func, *args, timeout, extra_env=None):
	"""
	Run a function in a sub-process

    Args:
            func: function, the function to be run. It must be in a module that is importable.
            *args: str. Any additional command line arguments to be passed in
                        the first argument to ``subprocess.run``.
            extra_env: dict[str, str]. Any additional environment variables to be set for the subprocess.
    Returns:
            CompletedProcess instance
	"""
	import subprocess
	import os
	import sys
	import tempfile
	import shutil
	import time
	import signal
	import traceback
	import threading
	import logging

	# Set up logging
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	handler = logging.StreamHandler()
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	# Set up a temporary directory
	temp_dir = tempfile.mkdtemp()
	logger.debug('Created temporary directory: {}'.format(temp_dir))

	# Set up a temporary file to store the output
	temp_file = os.path.join(temp_dir, 'output.txt')
	logger.debug('Created temporary file: {}'.format(temp_file))

	# Set up a temporary file to store the error
	temp_error = os.path.join(temp_dir, 'error.txt')
	logger.debug('Created temporary file: {}'.format(temp_error))

	# Set up a temporary file to store the return code
	temp_return_code = os.path.join(temp_dir, 'return_code.txt')
	logger.debug('Created temporary file: {}'.format(temp_return_code))

	# Set up a temporary file to store the exception
	temp_exception = os.path.join(temp_dir, 'exception.txt')
	logger.debug('Created temporary file: {}'.format(temp_exception))

	# Set up a temporary file to store the traceback
	temp_traceback = os.path.join(temp_dir, 'traceback.txt')
	logger.debug('Created temporary file: {}'.format(temp_traceback))

	# Set up a temporary file to store the stdout
	temp_stdout = os.path.join(temp_dir, 'stdout.txt')
	logger.debug('Created temporary file: {}'.format(temp_stdout))