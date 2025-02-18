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
        return class_name + '.' + extensions[0]
    else:
        best_extension = class_name + '.' + extensions[0]
        best_strength = (len(extensions[0]) - sum(c.isupper() for c in extensions[0])) - (len(extensions[0]) - sum(c.islower() for c in extensions[0]))
        for ext in extensions[1:]:
            strength = (len(ext) - sum(c.isupper() for c in ext)) - (len(ext) - sum(c.islower() for c in ext))
            if strength > best_strength:
                best_strength = strength
                best_extension = class_name + '.' + ext
            elif strength == best_strength and ext < best_extension:
                best_strength = strength
                best_extension = class_name + '.' + ext
        return best_extension
