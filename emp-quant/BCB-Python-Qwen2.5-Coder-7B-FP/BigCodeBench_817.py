from collections import Counter
import logging
def setup_logger(log_path):
    logger = logging.getLogger('task_func')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(log_path + '/task_func.log', encoding='utf-8')
    formatter = logging.Formatter('%(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
def task_func(letter_list, element, log_path):
    logger = setup_logger(log_path)
    logger.info(f"Function called with list: {letter_list} and element: {element}")
    
    if element not in letter_list:
        logger.error("The element is not in the letter list.")
        raise ValueError("The element is not in the letter list.")
    
    frequency = Counter(letter_list)[element]
    logger.info(f"Frequency of '{element}' is {frequency}")
    
    logger.shutdown()
    return frequency