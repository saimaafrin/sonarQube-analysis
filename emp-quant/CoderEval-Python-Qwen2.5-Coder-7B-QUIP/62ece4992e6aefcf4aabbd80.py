import os

def remove_ending_os_sep(input_list):
    if input_list is None:
        return []
    
    result = []
    for item in input_list:
        if len(item) > 1 and item[-1] == os.sep:
            result.append(item[:-1])
        else:
            result.append(item)
    
    return result