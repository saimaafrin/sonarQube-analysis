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

    # 1. You will have to use split() to split the string into a list of notes
    # 2. Then you will have to loop through each note and calculate how many beats it lasts using a dict
    # 3. Then you will have to append the calculated number of beats to a list
    # 4. Then you will return the list
    note_dict = {'o': 4, 'o|': 2, '.|': 1}
    note_list = music_string.split()
    beat_list = []
    for note in note_list:
        beat_list.append(note_dict[note])
    return beat_list
