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
    # Determine the number of rows and columns
    num_rows = len(PLANETS)
    num_cols = len(ELEMENTS)
    
    # Create a list of planet-element pairs
    planet_element_pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
    
    # Shuffle the list to ensure randomness
    random.shuffle(planet_element_pairs)
    
    # Create a DataFrame with the shuffled planet-element pairs
    df = pd.DataFrame(planet_element_pairs, columns=[f"Element_{i+1}" for i in range(num_cols)])
    
    # Reshape the DataFrame to have the correct number of rows and columns
    df = df.iloc[:num_rows, :num_cols]
    
    return df