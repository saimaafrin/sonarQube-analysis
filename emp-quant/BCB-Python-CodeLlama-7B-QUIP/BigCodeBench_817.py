
from collections import Counter
import logging

def task_func(letter_list, element, log_path):
    logging.basicConfig(filename=log_path, level=logging.DEBUG, encoding='utf-8')
    logging.info(f"Function called with list: {letter_list} and element: {element}")
    try:
        element_frequency = Counter(letter_list).get(element)
        logging.info(f"Frequency of '{element}' is {element_frequency}")
        return element_frequency
    except KeyError:
        logging.error(f"The element '{element}' is not in the letter list.")
        raise ValueError(f"The element '{element}' is not in the letter list.")
    finally:
        logging.shutdown()