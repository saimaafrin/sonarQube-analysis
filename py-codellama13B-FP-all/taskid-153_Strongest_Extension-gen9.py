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

    # Initialize an empty string as the strongest extension
    strongest_extension = ""
    # Initialize the strength of the extension as 0
    strength = 0
    # Loop over the extensions list
    for extension in extensions:
        # Initialize the strength of this extension as 0
        strength_of_this_extension = 0
        # Loop over the characters in the extension
        for character in extension:
            # If this character is an uppercase character
            if character.isupper():
                # Increment the strength of the extension
                strength_of_this_extension += 1
            # If this character is a lowercase character
            if character.islower():
                # Increment the strength of the extension
                strength_of_this_extension -= 1
        # If the strength of this extension is greater than the previous
        # strength of the strongest extension
        if strength_of_this_extension > strength:
            # Set the strongest extension to this extension
            strongest_extension = extension
            # Set the strength of the strongest extension to the strength of
            # this extension
            strength = strength_of_this_extension
    # Return the class name followed by the strongest extension
    return class_name + "." + strongest_extension
