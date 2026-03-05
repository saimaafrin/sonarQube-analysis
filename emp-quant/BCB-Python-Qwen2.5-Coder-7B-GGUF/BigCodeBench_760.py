
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
    
    names = latin_names + other_names
    df = pd.DataFrame(columns=['ID', 'Name', 'Date of Birth', 'Email'])
    
    for i in range(1, 101):
        name = np.random.choice(names)
        dob = np.random.randint(start_year, end_year + 1)
        dob = datetime.datetime(dob, np.random.randint(1, 13), np.random.randint(1, 28))
        email = re.sub(r'[^\w\s]+', '', name).lower() + str(dob.year) + '@' + email_domain
        
        df = df.append({'ID': i, 'Name': name, 'Date of Birth': dob, 'Email': email}, ignore_index=True)
    
    return df