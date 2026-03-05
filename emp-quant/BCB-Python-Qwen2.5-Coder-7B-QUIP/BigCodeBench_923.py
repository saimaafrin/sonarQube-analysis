
import pandas as pd
import random
import re

def task_func(person_names, email_domains, num_records=5):
    if len(person_names) < num_records:
        raise ValueError("The number of names provided is less than the number of records requested.")
    
    if not email_domains:
        raise ValueError("No email domains provided.")
    
    # Generate random names and emails
    names = random.sample(person_names, num_records)
    emails = [f"{name.replace(' ', '')}@{random.choice(email_domains)}" for name in names]
    
    # Clean emails by replacing "@" with "[at]"
    emails = [re.sub('@', '[at]', email) for email in emails]
    
    # Create DataFrame
    df = pd.DataFrame({'Name': names, 'Email': emails})
    
    return df

try:
    result_df = task_func(person_names, email_domains, num_records)
    print(result_df)
except ValueError as e:
    print(e)