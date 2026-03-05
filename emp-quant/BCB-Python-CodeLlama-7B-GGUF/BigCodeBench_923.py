
import pandas as pd
import random
import re

def task_func(person_names, email_domains, num_records=5):
    """
    Generate a DataFrame with a specified number of records containing personal names and emails.
    The emails are cleaned by replacing all occurrences of "@" with "[at]".
    """
    if len(person_names) < num_records:
        raise ValueError("Number of names provided is less than the number of records requested")
    if not email_domains:
        raise ValueError("No email domains provided")

    # Generate random emails
    emails = [f"{person_name}@{random.choice(email_domains)}" for person_name in person_names]

    # Clean emails by replacing "@" with "[at]"
    clean_emails = [re.sub(r"@", r"[at]", email) for email in emails]

    # Create DataFrame with columns 'Name' and 'Email'
    df = pd.DataFrame({"Name": person_names, "Email": clean_emails})

    return df