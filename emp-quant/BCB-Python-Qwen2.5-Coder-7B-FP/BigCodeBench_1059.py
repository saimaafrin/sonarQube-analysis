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
    Generates a DataFrame with random planet-element pairs.
    
    Returns:
        pandas.DataFrame: A DataFrame where each cell contains a string in the format 'Planet:Element'.
        The DataFrame has a number of rows equal to the number of planets and
        a number of columns equal to the number of elements.
    """
    # Ensure the number of planets and elements are the same for simplicity
    if len(PLANETS) != len(ELEMENTS):
        raise ValueError("The number of planets and elements must be the same.")
    
    # Generate all possible planet-element pairs
    pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
    
    # Shuffle the pairs to ensure randomness
    random.shuffle(pairs)
    
    # Create a DataFrame with the shuffled pairs
    df = pd.DataFrame(pairs).T
    
    return df