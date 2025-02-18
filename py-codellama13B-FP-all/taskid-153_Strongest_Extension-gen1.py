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

    # Initialize the extension with the lowest strength as the first element of the list.
    strongest = (0, extensions[0])
    # Iterate through all extensions
    for extension in extensions:
        # Calculate the strength of the extension
        cap = sum([1 for char in extension if char.isupper()])
        sm = sum([1 for char in extension if char.islower()])
        strength = cap - sm
        # If the strength of the current extension is greater than the stored strength,
        # update the stored strength and extension
        if strength > strongest[0]:
            strongest = (strength, extension)
    # Return the class name and the strongest extension
    return class_name + '.' + strongest[1]
