from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    """
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    >>> bf('Jupiter', 'Neptune')
    ('Saturn', 'Uranus')
    >>> bf('Earth', 'Mercury')
    'Venus'
    >>> bf('Mercury', 'Uranus')
    ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    """

    if planet1 not in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        return ()
    elif planet2 not in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        return ()
    elif planet1 == planet2:
        return ()
    elif planet1 == 'Mercury':
        if planet2 == 'Venus':
            return ('Venus',)
        elif planet2 == 'Earth':
            return ('Venus', 'Earth', 'Mars')
        elif planet2 == 'Mars':
            return ('Venus', 'Earth', 'Mars', 'Jupiter')
        elif planet2 == 'Jupiter':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
        elif planet2 == 'Saturn':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
        elif planet2 == 'Uranus':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
        elif planet2 == 'Neptune':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    elif planet1 == 'Venus':
        if planet2 == 'Earth':
            return ('Venus', 'Earth', 'Mars')
        elif planet2 == 'Mars':
            return ('Venus', 'Earth', 'Mars', 'Jupiter')
        elif planet2 == 'Jupiter':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
        elif planet2 == 'Saturn':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
        elif planet2 == 'Uranus':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
        elif planet2 == 'Neptune':
            return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    elif planet1 == 'Earth':
        if planet2 == 'Mars':
            return ('Mars',)
        elif planet2 == 'Jupiter':
            return ('Mars', 'Jupiter')
        elif planet2 == 'Saturn':
            return ('Mars', 'Jupiter', 'Saturn')
        elif planet2 == 'Uranus':
            return ('Mars', 'Jupiter', 'Saturn', 'Uranus')
        elif planet2 == 'Neptune':
            return ('Mars', 'Jupiter', 'Saturn
