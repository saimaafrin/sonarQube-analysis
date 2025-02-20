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

    planets = {
        'Mercury': 1,
        'Venus': 2,
        'Earth': 3,
        'Mars': 4,
        'Jupiter': 5,
        'Saturn': 6,
        'Uranus': 7,
        'Neptune': 8
    }

    if planet1 not in planets or planet2 not in planets:
        return tuple()

    start = planets[planet1]
    end = planets[planet2]

    if start > end:
        start, end = end, start

    if start == end:
        return (planet1, )

    if start + 1 == end:
        return (planet1, planet2)

    return tuple(planet for planet, pos in planets.items() if start < pos <= end)
