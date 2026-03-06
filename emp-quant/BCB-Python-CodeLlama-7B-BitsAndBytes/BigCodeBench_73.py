
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast

def task_func(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Create a pandas DataFrame from the EmailData table
    df = pd.read_sql_query("SELECT email, list FROM EmailData", conn)

    # Convert the list column to a list of integers
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and variance of the list for each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)

    # Plot the bar chart of sum, mean, and variance
    fig, ax = plt.subplots()
    ax.bar(df['email'], df['sum'], label='Sum')
    ax.bar(df['email'], df['mean'], label='Mean')
    ax.bar(df['email'], df['var'], label='Variance')
    ax.set_xlabel('Email')
    ax.set_ylabel('Sum, Mean, Variance')
    ax.legend()

    # Return the DataFrame and the matplotlib Axes object
    return df, ax