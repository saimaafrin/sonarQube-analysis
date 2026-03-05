
import pandas as pd
import random
import re

def task_func(person_names, email_domains, num_records=5):
    if len(person_names) < num_records:
        raise ValueError("The number of names provided is less than the number of records requested.")
    if not email_domains:
        raise ValueError("No email domains are provided.")
    
    names = random.choices(person_names, k=num_records)
    emails = [f"{name.lower().replace(' ', '')}@{random.choice(email_domains)}" for name in names]
    cleaned_emails = [re.sub(r'@', '[at]', email) for email in emails]
    
    df = pd.DataFrame({'Name': names, 'Email': cleaned_emails})
    return df