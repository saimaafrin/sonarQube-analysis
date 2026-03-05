
import numpy as np
import pandas as pd

def task_func(country_dict):
    # Generate a random GDP value for each country
    gdp_values = np.random.randint(10000000000, 100000000000, size=len(country_dict))

    # Create a DataFrame with the GDP values
    gdp_df = pd.DataFrame(gdp_values, index=country_dict.keys(), columns=['GDP'])

    return gdp_df