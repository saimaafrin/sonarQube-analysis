from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """


    def parse(string: str) -> List[int]:
        notes = []
        for char in string:
            if char == 'o':
                notes.append(4)
            elif char == '|':
                notes.append(2)
            else:
                notes.append(1)
        return notes

    # here is where you should parse the string

    return parse(music_string)
