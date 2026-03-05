
import pandas as pd
import numpy as np
import codecs
import re
import datetime

def task_func(start_year=1980, end_year=2000, email_domain='example.com',
           latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
           other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], 
           rng_seed=None):
    # Set random seed if provided
    if rng_seed is not None:
        np.random.seed(rng_seed)
    
    # Generate random dates between start and end years
    dates = np.random.randint(start_year, end_year, size=100)
    
    # Generate random names
    names = np.random.choice(latin_names + other_names, size=100)
    
    # Correct improperly encoded Latin characters in names
    names = [re.sub(r'[^\x00-\x7F]', '', name) for name in names]
    
    # Generate random emails
    emails = [f'{name}{date}@{email_domain}' for name, date in zip(names, dates)]
    
    # Create DataFrame
    df = pd.DataFrame({'ID': np.arange(1, 101),
                       'Name': names,
                       'Date of Birth': dates,
                       'Email': emails})
    
    return df