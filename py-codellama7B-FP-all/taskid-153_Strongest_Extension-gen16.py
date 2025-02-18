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

    # if not class_name or not extensions:
    #     return ''
    # if len(extensions) == 1:
    #     return class_name + '.' + extensions[0]

    # extensions_dict = {}
    # for ext in extensions:
    #     lowercase_ext = ext.lower()
    #     uppercase_ext = ext.upper()
    #     ext_length = len(ext)
    #     uppercase_length = len(uppercase_ext)
    #     lowercase_length = len(lowercase_ext)
    #     if ext_length in extensions_dict:
    #         if lowercase_length > extensions_dict[ext_length][1]:
    #             extensions_dict[ext_length] = [ext, uppercase_length]
    #     else:
    #         extensions_dict[ext_length] = [ext, uppercase_length]

    # strongest_extension = max(extensions_dict, key=extensions_dict.get)
    # strongest_extension_name = extensions_dict[strongest_extension][0]
    # return class_name + '.' + strongest_extension_name

    extensions_dict = {e: e.upper() for e in extensions}
    strongest_extension = max(extensions_dict, key=len)
    return class_name + '.' + strongest_extension
