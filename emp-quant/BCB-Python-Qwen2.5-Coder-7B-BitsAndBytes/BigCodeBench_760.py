
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
    
    # Correct improper encoding in Latin characters
    def correct_encoding(name):
        return codecs.decode(name.encode('utf-8'), 'unicode_escape')
    
    # Generate random names
    names = []
    for _ in range(100):
        if np.random.rand() < 0.5:
            name = np.random.choice(latin_names)
        else:
            name = np.random.choice(other_names)
        names.append(correct_encoding(name))
    
    # Generate random dates of birth
    dates_of_birth = [
        datetime.datetime(start_year + np.random.randint(end_year - start_year), 
                          np.random.randint(1, 13), 
                          np.random.randint(1, 28)).strftime('%Y-%m-%d') 
        for _ in range(100)
    ]
    
    # Construct emails
    emails = [f"{name.replace(' ', '').lower()}{dob[-4:]}@{email_domain}" for name, dob in zip(names, dates_of_birth)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'ID': range(1, 101),
        'Name': names,
        'Date of Birth': dates_of_birth,
        'Email': emails
    })
    
    return df