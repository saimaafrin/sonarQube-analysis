import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast
def task_func(db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)

    # Create a cursor object
    c = conn.cursor()

    # Execute a query to retrieve the data
    c.execute("SELECT email, list FROM EmailData")

    # Convert the list column to a list
    data = c.fetchall()
    data = [ast.literal_eval(row[1]) for row in data]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=['email', 'list'])

    # Calculate the sum, mean, and variance of the list for each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['email'], df['sum'], label='Sum')
    ax.bar(df['email'], df['mean'], label='Mean')
    ax.bar(df['email'], df['var'], label='Variance')
    ax.set_xlabel('Email')
    ax.set_ylabel('Value')
    ax.set_title('Sum, Mean, and Variance of Lists')
    ax.legend()

    # Close the cursor and connection
    c.close()
    conn.close()

    # Return the DataFrame and the Axes object
    return df, ax
db_file = 'email_data.db'