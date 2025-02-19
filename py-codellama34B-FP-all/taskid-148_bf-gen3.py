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

    # planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planets = {'Mercury': 0, 'Venus': 1, 'Earth': 2, 'Mars': 3, 'Jupiter': 4, 'Saturn': 5, 'Uranus': 6, 'Neptune': 7}
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    p1 = planets[planet1]
    p2 = planets[planet2]

    if p1 < p2:
        return tuple(planets[key] for key in sorted(planets.keys(), key=planets.get)[p1+1:p2+1])
    else:
        return tuple(planets[key] for key in sorted(planets.keys(), key=planets.get)[p2+1:p1+1])
