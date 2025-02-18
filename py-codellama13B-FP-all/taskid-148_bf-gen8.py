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


    # dictionary to map planet names to their order from the sun
    # (0 is closest to the sun, 7 is farthest)
    planets = {
        'Mercury': 0,
        'Venus': 1,
        'Earth': 2,
        'Mars': 3,
        'Jupiter': 4,
        'Saturn': 5,
        'Uranus': 6,
        'Neptune': 7
    }

    # get the orders of the planets
    try:
        order1 = planets[planet1]
        order2 = planets[planet2]
    except KeyError:
        return () # return empty tuple if planet name is incorrect

    # return all planets between the two orders
    return tuple(planet for planet, order in planets.items() if order1 < order < order2)
