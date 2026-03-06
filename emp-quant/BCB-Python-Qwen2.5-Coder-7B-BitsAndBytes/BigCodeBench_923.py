
import pandas as pd
import random
import re

def task_func(person_names, email_domains, num_records=5):
    # Check if the number of names is sufficient
    if len(person_names) < num_records:
        raise ValueError("Number of names provided is less than the number of records requested.")
    
    # Check if any email domains are provided
    if not email_domains:
        raise ValueError("No email domains provided.")
    
    # Initialize an empty list to store the data
    data = []
    
    # Generate the required number of records
    for _ in range(num_records):
        # Randomly select a name and an email domain
        name = random.choice(person_names)
        domain = random.choice(email_domains)
        
        # Create an email address
        email = f"{name.lower().replace(' ', '.')}@{domain}"
        
        # Clean the email by replacing "@" with "[at]"
        cleaned_email = re.sub(r'@', '[at]', email)
        
        # Append the data to the list
        data.append({'Name': name, 'Email': cleaned_email})
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    return df