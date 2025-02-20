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

    # Initialize variables
    strongest_extension = None
    strongest_extension_value = None
    current_extension_value = None

    # Iterate over the extensions list
    for extension in extensions:
        # Initialize variables
        uppercase_letter_count = 0
        lowercase_letter_count = 0

        # Iterate over the extension's name
        for char in extension:
            # Check if the current character is an uppercase letter
            if char.isupper():
                # Increment the uppercase letter counter
                uppercase_letter_count += 1
            # Check if the current character is a lowercase letter
            elif char.islower():
                # Increment the lowercase letter counter
                lowercase_letter_count += 1

        # Calculate the extension's value
        current_extension_value = uppercase_letter_count - lowercase_letter_count

        # Check if the current extension value is the strongest
        if (strongest_extension_value == None) or (current_extension_value > strongest_extension_value):
            # Set the current extension value as the new strongest extension value
            strongest_extension_value = current_extension_value
            # Set the current extension as the strongest extension
            strongest_extension = extension

    # Format and return the strongest extension
    return f"{class_name}.{strongest_extension}"
