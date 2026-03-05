
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
    num_planets = len(PLANETS)
    num_elements = len(ELEMENTS)
    
    # Generate all possible planet-element pairs
    planet_element_pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
    
    # Shuffle the pairs to ensure randomness
    random.shuffle(planet_element_pairs)
    
    # Create a DataFrame with the shuffled pairs
    df = pd.DataFrame(planet_element_pairs, columns=["Planet:Element"])
    
    # Reshape the DataFrame to have num_planets rows and num_elements columns
    df = df.values.reshape(num_planets, num_elements)
    df = pd.DataFrame(df, columns=[f"Element_{i+1}" for i in range(num_elements)])
    
    return df