import pandas as pd
import numpy as np
import codecs
import re
import datetime
def task_func(start_year=1980, end_year=2000, email_domain='example.com',
           latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
           other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'], 
           rng_seed=None):
    """
    Creates a random DataFrame with 100 records. Each record consists of an ID (ranging from 1 to 100), Name (randomly selected from provided lists of Latin and other names), Date of Birth (randomly generated dates between the specified years), and Email (constructed using the name, year of birth, and provided email domain). Improperly encoded Latin characters in names are corrected during the process.
    """
    # Set random seed if provided
    if rng_seed is not None:
        np.random.seed(rng_seed)

    # Generate random dates between start and end years
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # Generate random names
    names = np.random.choice(latin_names + other_names, size=100)

    # Correct improperly encoded Latin characters in names
    names = [re.sub(r'([a-z])([A-Z])', r'\1 \2', name) for name in names]

    # Generate random emails
    emails = [f"{name}{date.strftime('%y%m%d')}@{email_domain}" for name, date in zip(names, date_range)]

    # Create DataFrame
    df = pd.DataFrame({'ID': np.arange(1, 101), 'Name': names, 'Date of Birth': date_range, 'Email': emails})

    return df