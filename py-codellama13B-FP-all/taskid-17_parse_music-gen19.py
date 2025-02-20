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

    beats = []
    for symbol in music_string:
        if symbol == 'o':
            beats.append(4)
        elif symbol == '.':
            beats.append(1)
        elif symbol == '|':
            last_beat = beats.pop()
            if last_beat == 4:
                beats.append(2)
            else:
                raise ValueError(f"Invalid input: {music_string}")
        else:
            raise ValueError(f"Invalid input: {music_string}")
    return beats
