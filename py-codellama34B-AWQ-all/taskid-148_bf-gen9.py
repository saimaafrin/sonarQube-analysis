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

    def planet_distance_to_sun(planet: str) -> int:
        """
        The distance to sun is 0 for Mercury and 
        increases by 1 for each planet until Neptune
        """
        return {
            'Mercury': 0,
            'Venus': 1,
            'Earth': 2,
            'Mars': 3,
            'Jupiter': 4,
            'Saturn': 5,
            'Uranus': 6,
            'Neptune': 7
        }.get(planet, -1)
    
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    distance_planet1 = planet_distance_to_sun(planet1)
    distance_planet2 = planet_distance_to_sun(planet2)
    
    # check if planet names are valid
    if distance_planet1 == -1 or distance_planet2 == -1:
        return ()
    
    # get the position of both planets in the list
    position_planet1 = planets.index(planet1)
    position_planet2 = planets.index(planet2)
    
    # check the order and swap if necessary
    if position_planet1 > position_planet2:
        position_planet1, position_planet2 = position_planet2, position_planet1
    
    # get the list of planets between planet1 and planet2
    planets_between = planets[position_planet1:position_planet2]
    
    return tuple(planets_between)
