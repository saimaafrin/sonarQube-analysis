
import time
import threading

def task_func(delay_time: float = 1.0, num_threads: int = 5) -> list:
    def thread_task(thread_id: int):
        time.sleep(delay_time)
        return f'Delay in thread {thread_id} completed'

    threads = []
    results = []

    for i in range(num_threads):
        thread = threading.Thread(target=thread_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        results.append(thread_task(thread.ident))

    return results