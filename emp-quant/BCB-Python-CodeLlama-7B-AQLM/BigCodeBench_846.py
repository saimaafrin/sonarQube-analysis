import collections
import pandas as pd
def task_func(obj_list, attr):
    """
    Count the frequency of each value of the given attribute from a list of objects.
    
    This function returns a pandas Dataframe containing frequency count of the specified attribute from the objects in the list.
    The DataFrame consist of two columns ('attribute' and 'count'), which contain the attribute and its
    specific count respectively.
    
    If no attributes are found, an empty DataFrame is returned.

    Parameters:
    obj_list (list): The list of objects with attributes.
    attr (str): The attribute to count.

    Returns:
    collections.Counter: The frequency count of each value of the attribute.

    Requirements:
    - collections
    - pandas
    
    Example:
    >>> class ExampleObject:
    ...     def __init__(self, color, shape):
    ...         self.color = color
    ...         self.shape = shape
    ...
    >>> obj_list = [ExampleObject('Red', 'Square'), ExampleObject('Green', 'Circle'), ExampleObject('Red', 'Rectangle')]
    >>> count = task_func(obj_list, 'color')
    >>> print(count)
      attribute  count
    0       Red      2
    1     Green      1


    >>> class ExampleObject:
    ...     def __init__(self, animal, shape):
    ...         self.animal = animal
    ...         self.shape = shape
    ...
    >>> obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]
    >>> count = task_func(obj_list, 'shape')
    >>> print(count)
       attribute  count
    0     Square      1
    1     Circle      1
    2  Rectangle      2
    """
    if not obj_list:
        return pd.DataFrame()
    if not isinstance(obj_list, list):
        raise TypeError('obj_list must be a list.')
    if not isinstance(attr, str):
        raise TypeError('attr must be a string.')
    if not all(isinstance(obj, collections.abc.Mapping) for obj in obj_list):
        raise TypeError('obj_list must be a list of dictionaries.')
    if not all(isinstance(obj[attr], str) for obj in obj_list):
        raise TypeError('obj_list must be a list of dictionaries with string values for the attribute.')
    if not all(attr in obj for obj in obj_list):
        raise ValueError('obj_list must be a list of dictionaries with the attribute.')
    return pd.DataFrame(collections.Counter(obj[attr] for obj in obj_list), columns=['attribute', 'count'])