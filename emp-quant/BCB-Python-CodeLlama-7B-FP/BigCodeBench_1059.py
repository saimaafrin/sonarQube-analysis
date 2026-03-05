import numpy as np
import random
import itertools
import pandas as pd
PLANETS = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
ELEMENTS = [
    "Hydrogen",
    "Helium",
    "Oxygen",
    "Carbon",
    "Nitrogen",
    "Magnesium",
    "Silicon",
    "Iron",
    "Nickel",
]
def task_func():
    """
    Generate a DataFrame where each row contains random planet-element pairs.
    Each pair is formatted as 'Planet:Element'. The number of rows is determined
    by the number of planets, and each row will contain as many planet-element
    pairs as there are elements.
    """
    # Generate a list of random planet-element pairs
    planet_element_pairs = []
    for planet in PLANETS:
        for element in ELEMENTS:
            planet_element_pairs.append(f"{planet}:{element}")

    # Create a DataFrame with the planet-element pairs
    df = pd.DataFrame(planet_element_pairs, columns=["Planet:Element"])

    # Check that the DataFrame has the correct number of rows and columns
    assert df.shape[0] == len(PLANETS)
    assert df.shape[1] == len(ELEMENTS)

    return df