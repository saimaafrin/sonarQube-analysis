
import pandas as pd
import numpy as np
import codecs
import re
import datetime

def task_func(start_year=1980, end_year=2000, email_domain='example.com',
               latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
               other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], 
               rng_seed=None):
    # Set the random number generator seed
    if rng_seed is not None:
        np.random.seed(rng_seed)
    
    # Create a list of all names
    all_names = latin_names + other_names
    
    # Create a list of all years between start_year and end_year
    years = list(range(start_year, end_year + 1))
    
    # Create a list of all IDs
    ids = list(range(1, 101))
    
    # Create a list of all emails
    emails = []
    for name in all_names:
        for year in years:
            email = f"{name.lower()}{year}@{email_domain}"
            emails.append(email)
    
    # Create a list of all dates of birth
    dates_of_birth = []
    for year in years:
        for _ in range(100):
            month = np.random.randint(1, 13)
            day = np.random.randint(1, 32)
            date_of_birth = f"{year}-{month:02d}-{day:02d} 00:00:00"
            dates_of_birth.append(date_of_birth)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'ID': ids,
        'Name': all_names,
        'Date of Birth': dates_of_birth,
        'Email': emails
    })
    
    return df