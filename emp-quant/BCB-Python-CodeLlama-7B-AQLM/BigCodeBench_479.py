import random
import string
import pandas as pd
def task_func(data_list, seed=0):
    """
    Replace a random substring (a sequence of characters between two commas or at the beginning/end of the string)
    in a list of strings with a random string (comprising ascii lowercase characters) with the same length as
    the substituted characters.

    Parameters:
    data_list (list): Input list of strings.
                      Within each string, each substring's leading and trailing whitespaces are removed.
                      If empty, it will return a DataFrame with the Original String and Modified String
                      columns that is otherwise empty.
    seed (int, optional): The seed for random operations to ensure reproducibility. Defaults to 0.

    Returns:
    DataFrame: A pandas DataFrame with two columns - 'Original String' and 'Modified String'.
               'Original String' contains the original strings from the input list, and 'Modified String'
               contains the modified strings where a random substring has been replaced.

    Requirements:
    - pandas
    - random
    - string

    Example:
    >>> task_func(['lamp, bag, mirror', 'table, chair, bag, lamp'])
               Original String          Modified String
    0        lamp, bag, mirror        lamp, tkg, mirror
    1  table, chair, bag, lamp  table, chair, bag, kuhm
    """
    random.seed(seed)
    string.ascii_lowercase

    # Create a list of tuples where each tuple contains the original string and the modified string
    # where a random substring has been replaced.
    data = []
    for string in data_list:
        string = string.strip()
        if string == '':
            data.append(('', ''))
            continue
        string_list = string.split(',')
        modified_string = ''
        for i in range(len(string_list)):
            if i == 0:
                modified_string += string_list[i]
            else:
                modified_string += ',' + string_list[i]
        modified_string = modified_string.strip()
        random_index = random.randint(0, len(string_list) - 1)
        random_string = ''.join(random.choices(string.ascii_lowercase, k=len(string_list[random_index])))
        modified_string = modified_string.replace(string_list[random_index], random_string)
        data.append((string, modified_string))

    # Create a pandas DataFrame from the list of tuples.
    df = pd.DataFrame(data, columns=['Original String', 'Modified String'])
    return df