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

    class_name = class_name.lower()
    class_name_lowercase = len(list(filter(str.islower, class_name)))
    class_name_uppercase = len(list(filter(str.isupper, class_name)))
    class_strength = class_name_uppercase - class_name_lowercase

    best_extension_strength = 0
    best_extension = class_name

    for extension in extensions:
        extension = extension.lower()
        extension_lowercase = len(list(filter(str.islower, extension)))
        extension_uppercase = len(list(filter(str.isupper, extension)))
        extension_strength = extension_uppercase - extension_lowercase

        if extension_strength > best_extension_strength:
            best_extension = extension
            best_extension_strength = extension_strength

    return f"{class_name}.{best_extension}"
