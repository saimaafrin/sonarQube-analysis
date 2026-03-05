
from collections import Counter
import logging

def task_func(letter_list, element, log_path):
    # Configure logging
    logger = logging.getLogger('task_func')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_path + 'task_func.log', 'w', encoding='utf-8')
    logger.addHandler(file_handler)

    # Log function call
    logger.info(f"Function called with list: {letter_list} and element: {element}")

    # Count the frequency of the element
    letter_count = Counter(letter_list)
    element_frequency = letter_count[element] if element in letter_count else 0

    # Log the frequency
    logger.info(f"Frequency of '{element}' is {element_frequency}")

    # Remove the file handler to release the file
    logger.removeHandler(file_handler)

    # Raise exception if element is not in the list
    if element not in letter_list:
        logger.error(f"The element is not in the letter list.")
        raise ValueError("Element not in list")

    return element_frequency