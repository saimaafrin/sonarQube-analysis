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


    # Create a mapping of characters to their corresponding note length
    # You can ignore the dot ('.') because we'll get to it later
    note_length_dict = {
        '.': 0,
        'o': 4,
        '|': 2,
    }

    # Split the string into a list of characters
    notes = list(music_string)

    # Create an empty list to store the notes' lengths
    note_lengths = []

    # Iterate through the notes
    for note in notes:
        # Use the dictionary to get the length of the current note
        # And add that to the list
        note_lengths.append(note_length_dict[note])

    # Initialize the note length (i.e. the number of beats for the current note)
    # To 0, as we're starting with the first note
    note_length = 0

    # Iterate through the list of note lengths
    for i in range(len(note_lengths)):
        # If the current note is a dot ('.')
        # (Remember we ignored it in the dictionary?)
        # Add the length of the previous note to the dot's length
        # (i.e. if the previous note was a whole note, the dot makes it a half note)
        if note_lengths[i] == 0:
            note_lengths[i] = note_lengths[i - 1]

    return note_lengths
