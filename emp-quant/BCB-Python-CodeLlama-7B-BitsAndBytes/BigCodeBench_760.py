
import pandas as pd
import numpy as np
import codecs
import re
import datetime

def task_func(start_year=1980, end_year=2000, email_domain='example.com',
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
              rng_seed=None):
    # Generate random data
    np.random.seed(rng_seed)
    id_list = np.arange(1, 101)
    name_list = np.random.choice(latin_names + other_names, size=100)
    birth_date_list = np.random.randint(start_year, end_year, size=100)
    email_list = [f"{name}{birth_date}@{email_domain}" for name, birth_date in zip(name_list, birth_date_list)]

    # Correct improperly encoded Latin characters in names
    name_list = [re.sub(r'[^\x00-\x7F]', '', name) for name in name_list]

    # Create DataFrame
    df = pd.DataFrame({'ID': id_list, 'Name': name_list, 'Date of Birth': birth_date_list, 'Email': email_list})

    return df