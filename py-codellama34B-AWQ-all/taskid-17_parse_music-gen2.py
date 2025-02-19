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

    # This is a list which will store all the times
    times = []
    # This is a list which contains all the characters
    characters = list(music_string)
    # The whole note
    wn = 4
    # The half note
    hn = 2
    # The quater note
    qn = 1
    # The iterator
    i = 0

    # This while loop checks if the iterator is in range
    while i < len(characters):
        # The current character
        character = characters[i]
        # This if statement checks if the current character is a whole note
        if character == 'o':
            # This checks if the next character is a vertical bar
            if characters[i + 1] == '|':
                # This adds the whole note to the list
                times.append(wn)
                # This adds 2 to the iterator
                i += 2
            # This else statement checks if the next character is a space
            else:
                # This adds the whole note to the list
                times.append(wn)
                # This adds 1 to the iterator
                i += 1
        # This elif statement checks if the current character is a half note
        elif character == 'o' and characters[i + 1] == '|':
            # This adds the half note to the list
            times.append(hn)
            # This adds 2 to the iterator
            i += 2
        # This elif statement checks if the current character is a quater note
        elif character == '.':
            # This checks if the next character is a vertical bar
            if characters[i + 1] == '|':
                # This adds the quater note to the list
                times.append(qn)
                # This adds 2 to the iterator
                i += 2
            # This else statement checks if the next character is a space
            else:
                # This adds the quater note to the list
                times.append(qn)
                # This adds 1 to the iterator
                i += 1

        # This else statement checks if the current character is a space
        elif character == ' ':
            # This adds 1 to the iterator
            i += 1

    # This returns the list
    return times
