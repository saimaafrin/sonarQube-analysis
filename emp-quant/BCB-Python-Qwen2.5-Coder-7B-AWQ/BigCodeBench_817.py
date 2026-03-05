from collections import Counter
import logging
def setup_logger(log_path):
    # Configure the logger
    logger = logging.getLogger('task_func')
    logger.setLevel(logging.DEBUG)
    
    # Create file handler which logs even debug messages
    fh = logging.FileHandler(log_path + '/task_func.log', mode='w', encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(fh)
    return logger
def task_func(letter_list, element, log_path):
    logger = setup_logger(log_path)
    
    # Log function call
    logger.info(f"Function called with list: {letter_list} and element: {element}")
    
    # Check if the element is in the list
    if element not in letter_list:
        logger.error("The element is not in the letter list.")
        raise ValueError("The element is not in the letter list.")
    
    # Count the frequency of the element
    frequency = Counter(letter_list)[element]
    
    # Log the frequency
    logger.info(f"Frequency of '{element}' is {frequency}")
    
    # Shutdown the logger
    logger.shutdown()
    
    return frequency