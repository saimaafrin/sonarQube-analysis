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

    planets_dict = {'Mercury': 1,
                    'Venus': 2,
                    'Earth': 3,
                    'Mars': 4,
                    'Jupiter': 5,
                    'Saturn': 6,
                    'Uranus': 7,
                    'Neptune': 8}
    planet1_num = planets_dict.get(planet1)
    planet2_num = planets_dict.get(planet2)
    if planet1_num is None or planet2_num is None:
        return ()

    sorted_planets_names = list(planets_dict.keys())
    sorted_planets_names.sort(key=lambda x: planets_dict[x])
    result = []
    for planet in sorted_planets_names:
        if planets_dict[planet] > planet1_num and planets_dict[planet] < planet2_num:
            result.append(planet)
    return tuple(result)
