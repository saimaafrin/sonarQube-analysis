
import pandas as pd
import random
import re

def task_func(person_names, email_domains, num_records=5):
    """
    Generate a DataFrame with a specified number of records containing personal names and emails.
    The emails are cleaned by replacing all occurrences of "@" with "[at]".
    The function should raise the exception for:
        ValueError: If the number of names provided is less than the number of records requested or if no email domains are provided.
    The function should output with:
        DataFrame: A pandas DataFrame with columns 'Name' and 'Email' containing the person names and cleaned emails.
    """
    if len(person_names) < num_records:
        raise ValueError("Number of names provided is less than the number of records requested")
    if not email_domains:
        raise ValueError("No email domains provided")

    # Generate a list of random names and emails
    names = random.sample(person_names, num_records)
    emails = [f"{name}@example.com" for name in names]

    # Clean the emails by replacing all occurrences of "@" with "[at]"
    clean_emails = [re.sub(r"@", "[at]", email) for email in emails]

    # Create a DataFrame with the names and cleaned emails
    df = pd.DataFrame({"Name": names, "Email": clean_emails})

    return df

df = task_func(person_names, email_domains, num_records)
print(df)