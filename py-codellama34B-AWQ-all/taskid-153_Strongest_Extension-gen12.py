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

    def strength_of_extention(extention: str) -> float:
        """Calculates the strength of the extention based on the number of uppercase
        and lowercase letters in its name.
        """
        number_of_uppercase = 0
        for char in extention:
            if char.isupper():
                number_of_uppercase += 1
        number_of_lowercase = len(extention) - number_of_uppercase
        return number_of_uppercase - number_of_lowercase

    # Find the strongest extention.
    strongest_extension = extensions[0]
    max_strength = strength_of_extention(strongest_extension)
    for extention in extensions:
        strength = strength_of_extention(extention)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extention

    # Return the extention name in the correct format.
    return f'{class_name}.{strongest_extension}'
