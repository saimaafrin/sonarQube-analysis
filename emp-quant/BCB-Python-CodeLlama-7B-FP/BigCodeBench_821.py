import time
import threading
def task_func(delay_time: float = 1.0, num_threads: int = 5):
    """
    Introduces a delay of 'delay_time' seconds in a specified number of separate threads and returns the thread completion messages.
    """
    # Create a list to store the completion messages
    completion_messages = []

    # Create a list of threads
    threads = []

    # Create a delay function that takes a thread number as an argument
    def delay_function(thread_number):
        # Sleep for the specified delay time
        time.sleep(delay_time)

        # Create a completion message
        completion_message = f"Delay in thread {thread_number} completed"

        # Add the completion message to the list
        completion_messages.append(completion_message)

    # Create the threads
    for thread_number in range(num_threads):
        # Create a new thread
        thread = threading.Thread(target=delay_function, args=(thread_number,))

        # Add the thread to the list of threads
        threads.append(thread)

        # Start the thread
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Return the completion messages
    return completion_messages