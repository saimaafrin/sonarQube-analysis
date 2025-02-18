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


    # Initialize the strength of the extension to 0
    strength = 0
    
    # Initialize the strongest extension's name to an empty string
    strongest_extension = ''
    
    # Loop over the extensions
    for extension in extensions:
        # Find the number of uppercase letters in the current extension's name
        cap = sum(1 for letter in extension if letter.isupper())
        
        # Find the number of lowercase letters in the current extension's name
        sm = sum(1 for letter in extension if letter.islower())
        
        # Calculate the strength of the current extension
        current_strength = cap - sm
        
        # If the current strength is stronger than the previous strength, set the
        # current extension as the strongest extension
        if current_strength > strength:
            strength = current_strength
            strongest_extension = extension
            
    # Return the class name followed by the strongest extension's name
    return f'{class_name}.{strongest_extension}'
