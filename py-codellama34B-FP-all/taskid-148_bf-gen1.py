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

    planets = {'Mercury': 0, 'Venus': 1, 'Earth': 2, 'Mars': 3, 'Jupiter': 4, 'Saturn': 5, 'Uranus': 6, 'Neptune': 7}
    p1 = planets.get(planet1)
    p2 = planets.get(planet2)
    if (p1 is None) or (p2 is None):
        return tuple()
    if p1 > p2:
        p1, p2 = p2, p1
    return tuple(planets[p] for p in sorted(planets, key=planets.get, reverse=False) if p1 < planets[p] < p2)
