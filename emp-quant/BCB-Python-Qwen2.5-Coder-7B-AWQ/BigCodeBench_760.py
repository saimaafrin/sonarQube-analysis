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
    
    # Function to correct improper encoded Latin characters
    def correct_latin(name):
        return re.sub(r'[^\x00-\x7F]+', '', name)
    
    # Generate random data
    ids = np.arange(1, 101)
    names = np.random.choice(latin_names + other_names, 100)
    names = [correct_latin(name) for name in names]
    dob = np.random.randint(start_year, end_year + 1, 100)
    dob = [datetime.datetime(d, np.random.randint(1, 13), np.random.randint(1, 28)) for d in dob]
    emails = [f"{name.lower()}{dob[i].year}{dob[i].month:02d}{dob[i].day:02d}@{email_domain}" for i, name in enumerate(names)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'ID': ids,
        'Name': names,
        'Date of Birth': dob,
        'Email': emails
    })
    
    return df