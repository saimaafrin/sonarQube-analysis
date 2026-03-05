import time
import threading
def task_func(delay_time: float = 1.0, num_threads: int = 5):
    """
    Introduces a delay of 'delay_time' seconds in a specified number of separate threads and returns the thread completion messages.
    """
    # Create a list to store the thread completion messages
    completion_messages = []

    # Create a list of threads
    threads = []
    for i in range(num_threads):
        # Create a new thread
        t = threading.Thread(target=delay_task, args=(delay_time, i))
        threads.append(t)

    # Start the threads
    for t in threads:
        t.start()

    # Wait for the threads to complete
    for t in threads:
        t.join()

    # Return the completion messages
    return completion_messages
def delay_task(delay_time: float, thread_id: int):
    """
    Introduces a delay of 'delay_time' seconds in a separate thread.
    """
    # Sleep for the specified delay time
    time.sleep(delay_time)

    # Create a completion message
    completion_message = f"Delay in thread {thread_id} completed"

    # Add the completion message to the list
    completion_messages.append(completion_message)