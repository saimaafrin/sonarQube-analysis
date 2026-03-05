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
    # Generate all possible planet-element pairs
    pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
    
    # Shuffle the pairs to ensure randomness
    random.shuffle(pairs)
    
    # Create a DataFrame with the shuffled pairs
    df = pd.DataFrame(pairs, columns=["Planet:Element"])
    
    # Reshape the DataFrame to have the same number of rows as planets and columns as elements
    df = df.groupby(df.index // len(ELEMENTS)).transform(lambda x: x.values.reshape(-1, len(ELEMENTS)))
    
    return df