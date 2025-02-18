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

    if extensions == []:
        return class_name
    else:
        strongest_extension = []
        for extension in extensions:
            num_upper = 0
            num_lower = 0
            for char in extension:
                if char.isupper():
                    num_upper += 1
                elif char.islower():
                    num_lower += 1
            if strongest_extension == [] or (num_upper - num_lower) > (num_upper - num_lower):
                strongest_extension = [extension]
            elif (num_upper - num_lower) == (num_upper - num_lower):
                strongest_extension.append(extension)
        strongest_extension = sorted(strongest_extension)
        if len(strongest_extension) > 1:
            return class_name + '.' + strongest_extension[0]
        else:
            return class_name + '.' + strongest_extension[0]
