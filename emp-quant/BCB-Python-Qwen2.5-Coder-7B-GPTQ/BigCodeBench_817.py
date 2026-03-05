from collections import Counter
import logging
def setup_logger(log_path):
    # Configure logging
    logging.basicConfig(filename=log_path + 'task_func.log', level=logging.DEBUG, encoding='utf-8')
    logger = logging.getLogger()
    return logger
def task_func(letter_list, element, log_path):
    logger = setup_logger(log_path)
    
    # Log function call
    logger.info(f"Function called with list: {letter_list} and element: {element}")
    
    # Check if element is in the list
    if element not in letter_list:
        logger.error("The element is not in the letter list.")
        raise ValueError("The element is not in the letter list.")
    
    # Count the frequency of the element
    frequency = Counter(letter_list)[element]
    
    # Log the frequency
    logger.info(f"Frequency of '{element}' is {frequency}")
    
    # Shutdown logging
    logging.shutdown()
    
    return frequency