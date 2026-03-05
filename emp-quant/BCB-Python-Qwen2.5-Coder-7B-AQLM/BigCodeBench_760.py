
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
    latin_names = [codecs.decode(name, 'latin1').encode('ascii', 'ignore').decode('ascii') for name in latin_names]
    other_names = [codecs.decode(name, 'latin1').encode('ascii', 'ignore').decode('ascii') for name in other_names]
    
    # Combining names
    all_names = latin_names + other_names
    
    # Generating data
    ids = np.arange(1, 101)
    names = np.random.choice(all_names, size=100)
    dob = np.random.randint(start_year, end_year + 1, size=100)
    dob = [datetime.datetime(year, np.random.randint(1, 13), np.random.randint(1, 28)) for year in dob]
    emails = [f"{name.lower().replace(' ', '')}{dob[i].year}{email_domain}" for i, name in enumerate(names)]
    
    # Creating DataFrame
    df = pd.DataFrame({
        'ID': ids,
        'Name': names,
        'Date of Birth': dob,
        'Email': emails
    })
    
    return df