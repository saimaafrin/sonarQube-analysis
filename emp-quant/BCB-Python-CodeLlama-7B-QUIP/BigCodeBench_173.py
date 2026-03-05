
import numpy as np
import pandas as pd

def task_func(country_dict):
    # Create a list of country names
    country_list = list(country_dict.keys())

    # Generate a random GDP value for each country
    gdp_values = np.random.randint(1000000000, 10000000000, len(country_list))

    # Create a DataFrame with the country names and GDP values
    df = pd.DataFrame(index=country_list, columns=['GDP'])
    df['GDP'] = gdp_values

    return df