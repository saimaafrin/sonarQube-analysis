
import numpy as np
import pandas as pd

def task_func(country_dict):
    # Create a list of country names
    country_names = list(country_dict.keys())

    # Generate random GDP values for each country
    gdp_values = np.random.randint(1000000000, 10000000000, size=len(country_names))

    # Create a DataFrame with country names and GDP values
    df = pd.DataFrame({'Country': country_names, 'GDP': gdp_values})

    return df