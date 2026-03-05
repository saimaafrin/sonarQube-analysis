
import numpy as np
import pandas as pd

def task_func(country_dict):
    # Define the GDP range
    min_gdp = 1_000_000_000
    max_gdp = 100_000_000_000

    # Create a DataFrame with countries as the index and random GDP values
    gdp_data = pd.DataFrame({
        'GDP': np.random.randint(min_gdp, max_gdp, size=len(country_dict))
    }, index=country_dict.keys())

    return gdp_data