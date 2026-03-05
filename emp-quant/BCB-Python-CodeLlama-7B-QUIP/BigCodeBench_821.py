
import time
import threading

def task_func(delay_time: float = 1.0, num_threads: int = 5):
    # Create a list to store the completion messages
    completion_messages = []

    # Create a list of threads
    threads = []
    for i in range(num_threads):
        # Create a thread
        thread = threading.Thread(target=task_func, args=(delay_time,))
        # Add the thread to the list
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to finish
    for thread in threads:
        thread.join()

    # Return the completion messages
    return completion_messages

# Define the task function
def task_func(delay_time: float = 1.0, num_threads: int = 5):
    # Create a list to store the completion messages
    completion_messages = []

    # Create a list of threads
    threads = []
    for i in range(num_threads):
        # Create a thread
        thread = threading.Thread(target=task_func, args=(delay_time,))
        # Add the thread to the list
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to finish
    for thread in threads:
        thread.join()

    # Return the completion messages
    return completion_messages

    # Call the function
    completion_messages = task_func(delay_time, num_threads)

    # Print the completion messages
    for completion_message in completion_messages:
        print(completion_message)