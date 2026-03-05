
import pandas as pd
import random
import re

def task_func(person_names, email_domains, num_records=5):
    if len(person_names) < num_records:
        raise ValueError("Number of names provided is less than the number of records requested")
    if not email_domains:
        raise ValueError("No email domains provided")
    names = random.sample(person_names, num_records)
    emails = [name + "@" + domain for name, domain in zip(names, email_domains)]
    return pd.DataFrame({"Name": names, "Email": emails})