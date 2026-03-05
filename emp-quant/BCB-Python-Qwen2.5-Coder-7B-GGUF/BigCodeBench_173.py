
import numpy as np
import pandas as pd

def task_func(country_dict):
    # Define the GDP range
    gdp_min = 1_000_000_000
    gdp_max = 100_000_000_000
    
    # Create a dictionary to store the GDP values
    gdp_values = {country: np.random.randint(gdp_min, gdp_max) for country in country_dict}
    
    # Create a DataFrame from the GDP values
    df = pd.DataFrame(list(gdp_values.items()), columns=['Country', 'GDP'])
    
    # Set the 'Country' column as the index
    df.set_index('Country', inplace=True)
    
    return df