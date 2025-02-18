from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    >>> Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
    'my_class.AA'
    """

    if len(extensions) == 0:
        return class_name
    
    # Initialize a dictionary with the extension strength (lowercase count) as key
    # and the extension as value
    extensions_dict = {
        len(e) - e.lower().count(e.lower()): e
        for e in extensions
    }
    
    # Sort the dictionary by value (lowercase count)
    # Reverse the sort order (so the highest counts are at the end)
    sorted_extensions = sorted(
        extensions_dict.items(), 
        key=lambda item: item[0], 
        reverse=True
    )
    
    # Return the extension name
    return f"{class_name}.{sorted_extensions[0][1]}"
