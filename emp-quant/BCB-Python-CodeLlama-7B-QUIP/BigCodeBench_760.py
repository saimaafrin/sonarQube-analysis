
import pandas as pd
import numpy as np
import codecs
import re
import datetime

def task_func(start_year=1980, end_year=2000, email_domain='example.com',
           latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
           other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], 
           rng_seed=None):
    np.random.seed(rng_seed)
    id_list = np.arange(1, 101)
    name_list = np.random.choice(latin_names + other_names, size=100, replace=True)
    date_of_birth_list = np.random.randint(start_year, end_year, size=100)
    date_of_birth_list = np.datetime64(date_of_birth_list, 'ns')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_birth_list.astype('datetime64[ns]')
    date_of_birth_list = date_of_