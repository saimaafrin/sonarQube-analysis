
from collections import Counter
import logging

def task_func(letter_list, element, log_path):
    # Set up logging
    logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.DEBUG)

    # Log function call
    logging.info(f"Function called with list: {letter_list} and element: {element}")

    # Count frequency of element in letter_list
    element_frequency = Counter(letter_list).get(element, 0)

    # Log frequency of element
    logging.info(f"Frequency of '{element}' is {element_frequency}")

    # Shut down logging
    logging.shutdown()

    return element_frequency