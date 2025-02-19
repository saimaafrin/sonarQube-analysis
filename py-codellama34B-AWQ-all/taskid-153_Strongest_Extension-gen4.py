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

    # Get the list of extensions' names
    extensions_names = [extension_name for extension_name in extensions]

    # Get the list of extensions' strength
    extensions_strength = [0 for extension_strength in extensions]
    for i, extension_strength in enumerate(extensions):
        cap_letters = [letter for letter in extension_strength if letter.isupper()]
        sm_letters = [letter for letter in extension_strength if letter.islower()]
        extensions_strength[i] = len(cap_letters) - len(sm_letters)

    # Get the strongest extension
    max_extension_strength = max(extensions_strength)
    strongest_extension = extensions_names[extensions_strength.index(max_extension_strength)]

    # Return the strongest extension
    return f'{class_name}.{strongest_extension}'
