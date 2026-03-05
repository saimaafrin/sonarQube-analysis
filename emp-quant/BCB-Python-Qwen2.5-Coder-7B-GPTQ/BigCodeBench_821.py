import time
import threading
def task_func(delay_time: float = 1.0, num_threads: int = 5):
    results = []

    def thread_task(thread_id):
        time.sleep(delay_time)
        results.append(f'Delay in thread {thread_id} completed')

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results