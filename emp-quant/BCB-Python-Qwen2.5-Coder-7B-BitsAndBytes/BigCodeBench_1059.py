
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
    pairs = list(itertools.product(PLANETS, ELEMENTS))
    
    # Shuffle the pairs randomly
    random.shuffle(pairs)
    
    # Create a DataFrame with the shuffled pairs
    df = pd.DataFrame(pairs[:num_planets * num_elements], 
                      index=range(num_planets), 
                      columns=range(num_elements))
    
    # Format the DataFrame cells as 'Planet:Element'
    df = df.applymap(lambda x: f"{x[0]}:{x[1]}")
    
    return df