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


    class_strength = 0
    for extension in extensions:
        uppercase_letters_count = 0
        lowercase_letters_count = 0
        for char in extension:
            if char.isupper():
                uppercase_letters_count += 1
            elif char.islower():
                lowercase_letters_count += 1
        
        strength = uppercase_letters_count - lowercase_letters_count
        if strength > class_strength:
            class_strength = strength
            extension_name = extension

    return '{}.{}'.format(class_name, extension_name)
