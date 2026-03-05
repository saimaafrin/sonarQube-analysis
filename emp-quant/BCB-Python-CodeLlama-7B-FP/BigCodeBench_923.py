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
    if len(person_names) < num_records or not email_domains:
        raise ValueError("Invalid input")

    # Generate a list of random emails
    emails = [f"{person_name}@{random.choice(email_domains)}" for person_name in person_names]

    # Replace all occurrences of "@" with "[at]"
    emails = [re.sub(r"@", r"[at]", email) for email in emails]

    # Create a DataFrame with the cleaned emails
    df = pd.DataFrame({"Name": person_names, "Email": emails})

    return df
person_names = ["John", "Jane", "Bob", "Alice"]
email_domains = ["example.com", "example.org"]