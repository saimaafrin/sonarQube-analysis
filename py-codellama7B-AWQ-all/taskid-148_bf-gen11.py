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

    planets = ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    index_p1 = planets.index(planet1)
    index_p2 = planets.index(planet2)
    if index_p1 == -1 or index_p2 == -1:
        return ()
    else:
        return tuple(planets[index_p1 + 1:index_p2])
