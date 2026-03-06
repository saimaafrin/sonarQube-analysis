
import numpy as np
import pandas as pd

def task_func(country_dict):
    # Define the GDP range
    gdp_min = 1_000_000_000
    gdp_max = 100_000_000_000
    
    # Generate random GDP values for each country
    gdp_values = {country: np.random.randint(gdp_min, gdp_max) for country in country_dict}
    
    # Create a DataFrame from the dictionary
    df_gdp = pd.DataFrame(list(gdp_values.items()), columns=['Country', 'GDP'])
    
    return df_gdp.set_index('Country')