
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
    
    # Create a list of planet-element pairs
    planet_element_pairs = [f"{planet}:{element}" for planet in PLANETS for element in ELEMENTS]
    
    # Shuffle the list to ensure randomness
    random.shuffle(planet_element_pairs)
    
    # Create a DataFrame with the shuffled pairs
    df = pd.DataFrame(planet_element_pairs).reshape(num_planets, num_elements)
    
    return df