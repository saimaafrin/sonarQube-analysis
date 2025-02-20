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

    # use a dictionary to map the extension to its strength.
    # initialize the dictionary with the first extension's name and its strength
    extension_strength = {extensions[0]: get_extension_strength(extensions[0])}
    for i in range(1, len(extensions)):
        extension = extensions[i]
        # if the extension is already in the dictionary, we don't need to add it
        if extension not in extension_strength:
            extension_strength[extension] = get_extension_strength(extension)
    # find the extension with the highest strength
    strongest_extension = max(extension_strength, key=extension_strength.get)
    return f'{class_name}.{strongest_extension}'
