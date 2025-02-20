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

    #TODO: Implement this
    # 2.1. 받은 클래스 이름과 확장 리스트에서 최대 확장 파일을 찾는다
    # 2.2. 확장 파일에 대해 클래스 이름과 확장 이름을 덧붙인 문자열을 반환한다
    # 2.3. 만약 확장 파일 중 같은 수의 대문자와 소문자 수가 있다면 처음 등장한 확장 파일을 반환한다
    # 2.4. 만약 확장 파일이 없다면 빈 문자열을 반환한다
    max_len = 0
    max_idx = -1
    for idx, extension in enumerate(extensions):
        if len(extension) == max_len:
            max_idx = max(max_idx, idx)
        else:
            max_len = len(extension)
            max_idx = idx
    if max_len != 0:
        return f"{class_name}.{extensions[max_idx]}"
    return ''
