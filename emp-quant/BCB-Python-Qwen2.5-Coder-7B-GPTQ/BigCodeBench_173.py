import numpy as np
import pandas as pd
def task_func(country_dict):
    # Define the GDP range
    gdp_min = 1_000_000_000
    gdp_max = 100_000_000_000
    
    # Generate random GDP values for each country
    gdp_values = np.random.randint(gdp_min, gdp_max + 1, size=len(country_dict))
    
    # Create a DataFrame with countries as index and GDP values as column
    gdp_df = pd.DataFrame(gdp_values, index=country_dict.keys(), columns=['GDP'])
    
    return gdp_df