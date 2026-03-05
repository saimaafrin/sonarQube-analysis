
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast

def task_func(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    # Create a pandas DataFrame from the SQLite table
    df = pd.read_sql("SELECT * FROM EmailData", conn)
    # Convert the list column to a list
    df['list'] = df['list'].apply(ast.literal_eval)
    # Calculate the sum, mean, and variance of the list for each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    # Plot the bar chart of sum, mean, and variance
    fig, ax = plt.subplots()
    ax.bar(df['sum'], df['mean'], df['var'])
    ax.set_xlabel('Sum')
    ax.set_ylabel('Mean')
    ax.set_title('Sum, Mean, and Variance')
    return df, fig, ax