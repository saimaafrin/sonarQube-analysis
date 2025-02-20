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

    # TODO: write your code here
    music_list = []
    beat = 0

    for char in music_string:
        if char == 'o':
            beat = 4
        elif char == '|':
            music_list.append(beat)
            beat = 0
        elif char == '.':
            beat = 1
        else:
            beat = 0

    return music_list
