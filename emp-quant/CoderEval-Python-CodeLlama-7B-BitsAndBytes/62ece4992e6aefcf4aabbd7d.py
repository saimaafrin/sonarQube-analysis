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
	import sys
	import os
	import tempfile
	import shutil
	import time
	import signal
	import traceback
	import threading
	import multiprocessing
	import multiprocessing.connection
	import multiprocessing.managers
	import multiprocessing.shared_memory
	import multiprocessing.synchronize
	import multiprocessing.pool
	import multiprocessing.queues
	import multiprocessing.util
	import multiprocessing.reduction
	import multiprocessing.pool
	import multiprocessing.managers
	import multiprocessing.shared_memory
	import multiprocessing.synchronize
	import multiprocessing.pool
	import multiprocessing.queues
	import multiprocessing.util
	import multiprocessing.reduction
	import multiprocessing.pool
	import multiprocessing.managers
	import multiprocessing.shared_memory
	import multiprocessing.synchronize
	import multiprocessing.pool
	import multiprocessing.queues
	import multiprocessing.util
	import multiprocessing.reduction
	import multiprocessing.pool
	import multiprocessing.managers
	import multiprocessing.shared_memory
	import multiprocessing.synchronize
	import multiprocessing.pool
	import multiprocessing.queues
	import multiprocessing.util
	import multiprocessing.reduction
	import multiprocessing.pool
	import multiprocessing.managers
	import multiprocessing.shared_memory
	import multiprocessing.synchronize
	import multiprocessing.pool
	import multiprocessing.queues
	import multiprocessing.util
	import multiprocessing.reduction
	import multiprocessing.pool
	import multiprocessing.managers
	import multiprocessing.shared_memory
	import multiprocessing.synchronize
	import multiprocessing.pool
	import multiprocessing.queues
	import multiprocessing.util