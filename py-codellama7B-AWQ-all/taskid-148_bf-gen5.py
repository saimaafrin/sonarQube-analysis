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


    # This function will return a list of the planets in the right order
    def get_planets(planet1: str, planet2: str) -> Tuple[str, ...]:
        planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn',
                   'Uranus', 'Neptune')
        if planet1 not in planets or planet2 not in planets:
            return ()
        return planets[planets.index(planet1):planets.index(planet2) + 1]
    return get_planets(planet1, planet2)
