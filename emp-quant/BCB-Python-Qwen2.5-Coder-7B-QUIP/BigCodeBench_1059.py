
import numpy as np
import random
import itertools
import pandas as pd
# Constants
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
    # Generate a DataFrame with random planet-element pairs
    num_planets = len(PLANETS)
    num_elements = len(ELEMENTS)
    data = []
    for _ in range(num_planets):
        pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
        data.append(pairs)
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=[f"Element_{i}" for i in range(num_elements)])
    
    return df