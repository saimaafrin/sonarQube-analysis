import subprocess
import os
import threading
def task_func(script_path: str, timeout: int = 60) -> str:
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The file {script_path} does not exist.")

    def run_script():
        try:
            result = subprocess.run(['python', script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}")

    process = threading.Thread(target=run_script)
    process.start()

    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        return "Terminating process due to timeout."
    else:
        return "Script executed successfully."