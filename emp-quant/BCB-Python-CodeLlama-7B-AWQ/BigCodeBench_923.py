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
        raise ValueError("The number of names provided is less than the number of records requested")
    if not email_domains:
        raise ValueError("No email domains are provided")

    # Generate a list of names and emails
    names = []
    emails = []
    for i in range(num_records):
        name = random.choice(person_names)
        email = f"{name}@{random.choice(email_domains)}"
        names.append(name)
        emails.append(email)

    # Create a DataFrame with the generated data
    df = pd.DataFrame({"Name": names, "Email": emails})

    # Clean the emails by replacing all occurrences of "@" with "[at]"
    df["Email"] = df["Email"].str.replace("@", "[at]")

    return df
person_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
email_domains = ["example.com", "example.org", "example.net"]