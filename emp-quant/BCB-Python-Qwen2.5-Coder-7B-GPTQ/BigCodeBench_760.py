import pandas as pd
import numpy as np
import codecs
import re
import datetime
def task_func(start_year=1980, end_year=2000, email_domain='example.com',
               latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
               other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], 
               rng_seed=None):
    if rng_seed is not None:
        np.random.seed(rng_seed)
    
    # Correcting improperly encoded Latin characters
    def correct_latin(name):
        return codecs.decode(name, 'latin1').encode('ascii', 'ignore').decode('utf-8')
    
    # Generate random data
    ids = np.arange(1, 101)
    names = np.random.choice(latin_names + other_names, 100)
    names = [correct_latin(name) for name in names]
    dob_years = np.random.randint(start_year, end_year + 1, 100)
    dob_months = np.random.randint(1, 13, 100)
    dob_days = np.random.randint(1, 28, 100)  # Simplified for demonstration
    dob = [datetime.datetime(year, month, day) for year, month, day in zip(dob_years, dob_months, dob_days)]
    emails = [f"{name.lower()}{year}@{email_domain}" for name, year in zip(names, dob_years)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'ID': ids,
        'Name': names,
        'Date of Birth': dob,
        'Email': emails
    })
    
    return df