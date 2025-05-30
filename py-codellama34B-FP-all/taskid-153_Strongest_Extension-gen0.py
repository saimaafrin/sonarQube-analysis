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
    for i in class_name:
        if i.isupper():
            class_strength += 1
        else:
            class_strength -= 1

    ext_strength = 0
    extension_list = []
    for extension in extensions:
        for i in extension:
            if i.isupper():
                ext_strength += 1
            else:
                ext_strength -= 1
        extension_list.append(ext_strength)
        ext_strength = 0
    max_strength = max(extension_list)
    for i, strength in enumerate(extension_list):
        if strength == max_strength:
            return f"{class_name}.{extensions[i]}"
