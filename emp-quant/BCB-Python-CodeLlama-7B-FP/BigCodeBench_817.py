from collections import Counter
import logging
def task_func(letter_list, element, log_path):
    """
    Count the frequency of a particular letter in a given list of letters with logging.
    Logs are written to a file named 'task_func.log' with encoding 'utf-8' and logging level DEBUG.
    The log file is created by the function or overwritten if already exists.
    For each function call the following is logged with the respective logging level:
        - info: f"Function called with list: {letter_list} and element: {element}"
        - error: if the element is not in the letter list
        - info: f"Frequency of '{element}' is {element_frequency}"
    After the last info has been logged, the logging is shutdown, such that all files are released.
    """
    # Set up logging
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)
    logging.info(f"Function called with list: {letter_list} and element: {element}")

    # Count the frequency of the element in the list
    element_frequency = Counter(letter_list)[element]

    # Log the frequency
    logging.info(f"Frequency of '{element}' is {element_frequency}")

    # Shutdown logging
    logging.shutdown()

    # Return the frequency
    return element_frequency