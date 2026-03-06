
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(data, date_format, country, country_codes=None):
    # Check if data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")
    
    # Check if date_format is a string
    if not isinstance(date_format, str):
        raise ValueError("Date format must be a string")
    
    # Check if country is in country_codes
    if country_codes is not None and country not in country_codes.values():
        raise ValueError(f"Country '{country}' not found in country codes")
    
    # Convert the data to the specified date format
    data['date'] = pd.to_datetime(data['date'], format=date_format)
    
    # Filter the data based on the country
    if country_codes is not None:
        data = data[data['country_code'].isin(country_codes[country])]
    
    # Draw a histogram of the dates
    ax = data['date'].hist(bins=30, figsize=(10, 6))
    
    # Set the title and labels
    ax.set_title('Date Distribution')
    ax.set_xlabel('Date')
    ax.set_ylabel('Frequency')
    
    return ax