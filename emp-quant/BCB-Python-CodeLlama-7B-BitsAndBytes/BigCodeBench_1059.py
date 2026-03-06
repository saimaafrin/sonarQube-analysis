
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
    # Generate a list of random planet-element pairs
    planet_element_pairs = []
    for planet in PLANETS:
        for element in ELEMENTS:
            planet_element_pairs.append(f"{planet}:{element}")

    # Create a DataFrame with the planet-element pairs
    df = pd.DataFrame(planet_element_pairs, columns=["Planet:Element"])

    # Shuffle the rows of the DataFrame
    df = df.sample(frac=1)

    return df

# Call the function and print the resulting DataFrame
df = task_func()
print(df)