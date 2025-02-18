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

    strongest = ['', 10000]
    for extension in extensions:
        cap_count = sum(map(lambda x: 1 if x.isupper() else 0, extension))
        sm_count = sum(map(lambda x: 1 if x.islower() else 0, extension))
        strength = cap_count - sm_count
        if strength < strongest[1]:
            strongest = [extension, strength]
        elif strength == strongest[1]:
            strongest = [extension, strength]
    
    return f'{class_name}.{strongest[0]}'
