import time
import threading
def task_func(delay_time: float = 1.0, num_threads: int = 5):
    """
    Introduces a delay of 'delay_time' seconds in a specified number of separate threads and returns the thread completion messages.
    """
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=delay_task, args=(delay_time, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return [f"Delay in thread {i} completed" for i in range(num_threads)]
def delay_task(delay_time: float, i: int):
    """
    Delays the execution of the task by 'delay_time' seconds.
    """
    time.sleep(delay_time)
    return f"Delay in thread {i} completed"