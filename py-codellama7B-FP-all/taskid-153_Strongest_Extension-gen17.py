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

    extensions_strength = {}
    for ext in extensions:
        lowercase = 0
        uppercase = 0
        for char in ext:
            if char.islower():
                lowercase += 1
            elif char.isupper():
                uppercase += 1
        extensions_strength[ext] = uppercase - lowercase
    # find the extension with the highest strength
    extension = ''
    max_strength = 0
    for ext, strength in extensions_strength.items():
        if strength > max_strength:
            extension = ext
            max_strength = strength
    return f'{class_name}.{extension}'
