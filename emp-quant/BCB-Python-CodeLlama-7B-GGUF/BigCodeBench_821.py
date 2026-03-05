
import time
import threading

def task_func(delay_time: float = 1.0, num_threads: int = 5):
    # Create a list to store the completion messages
    completion_messages = []

    # Create a list of threads
    threads = []
    for i in range(num_threads):
        # Create a new thread
        t = threading.Thread(target=delay_task, args=(delay_time, i))
        # Add the thread to the list of threads
        threads.append(t)

    # Start the threads
    for t in threads:
        t.start()

    # Wait for the threads to complete
    for t in threads:
        t.join()

    # Return the completion messages
    return [f"Delay in thread {i} completed" for i in range(num_threads)]

def delay_task(delay_time: float, thread_id: int):
    # Simulate a delay
    time.sleep(delay_time)
    # Return the completion message
    return f"Delay in thread {thread_id} completed"