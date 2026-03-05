
from collections import Counter
import logging

def task_func(letter_list, element, log_path):
    # Configure logging
    logging.basicConfig(filename=f"{log_path}/task_func.log", encoding='utf-8', level=logging.DEBUG)
    logger = logging.getLogger()

    # Log function call
    logger.info(f"Function called with list: {letter_list} and element: {element}")

    # Check if element is in the letter list
    if element not in letter_list:
        logger.error("The element is not in the letter list.")
        raise ValueError("The element is not in the letter list.")

    # Count the frequency of the element in the list
    frequency = Counter(letter_list)[element]

    # Log the frequency
    logger.info(f"Frequency of '{element}' is {frequency}")

    # Shutdown logging
    logging.shutdown()

    # Return the frequency
    return frequency