import pandas as pd
import random
import re
def task_func(person_names, email_domains, num_records=5):
    # Check if the number of names is less than the number of records requested
    if len(person_names) < num_records:
        raise ValueError("The number of names provided is less than the number of records requested.")
    
    # Check if no email domains are provided
    if not email_domains:
        raise ValueError("No email domains provided.")
    
    # Initialize an empty list to store the data
    data = []
    
    # Loop to generate the required number of records
    for _ in range(num_records):
        # Randomly select a person's name
        name = random.choice(person_names)
        
        # Randomly select an email domain
        domain = random.choice(email_domains)
        
        # Create an email by combining the name and domain
        email = f"{name.lower()}@{domain}"
        
        # Clean the email by replacing "@" with "[at]"
        cleaned_email = re.sub(r'@', '[at]', email)
        
        # Append the name and cleaned email to the data list
        data.append({'Name': name, 'Email': cleaned_email})
    
    # Create a pandas DataFrame from the data list
    df = pd.DataFrame(data)
    
    # Return the DataFrame
    return df