
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script not found: {script_path}")

    process = None
    try:
        process = subprocess.Popen(
            [script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.nice(19)  # Set process priority to low
        )

        start_time = time.time()
        cpu_usage = 0.0
        memory_usage = 0.0

        while process.poll() is None:
            time.sleep(0.1)
            if time.time() - start_time > timeout:
                process.terminate()
                raise TimeoutError(f"Script exceeded the timeout of {timeout} seconds")

            # Get the process object
            p = psutil.Process(process.pid)
            cpu_usage += p.cpu_percent(interval=0.1)
            memory_usage += p.memory_info().rss

        # Wait for the process to finish
        process.wait()

    except (subprocess.CalledProcessError, TimeoutError) as e:
        print(f"Error executing script: {e}")
        return {'CPU Usage': 0.0, 'Memory Usage': 0.0}

    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }