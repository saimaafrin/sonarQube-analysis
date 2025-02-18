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


    valid_planets = {
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    }

    def distance(planet: str) -> float:
        return {
            "Mercury": 0.38709898,
            "Venus": 0.72333617,
            "Earth": 1.0,
            "Mars": 1.38294622,
            "Jupiter": 5.20255683,
            "Saturn": 8.90080452,
            "Uranus": 19.1881284,
            "Neptune": 29.8655282,
        }[planet]

    if planet1 not in valid_planets or planet2 not in valid_planets:
        return ()

    distance1 = distance(planet1)
    distance2 = distance(planet2)

    planets = tuple(sorted(
        valid_planets,
        key=lambda x: distance(x),
    ))

    return tuple(filter(
        lambda x: distance1 < distance(x) < distance2,
        planets,
    ))
