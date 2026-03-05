
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast
def task_func(db_file):
    # Load data from SQLite database
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    conn.close()

    # Convert the 'list' column from string to list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate sum, mean, and variance for each list
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)

    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(df.index, df['sum'], label='Sum')
    ax.bar(df.index, df['mean'], label='Mean')
    ax.bar(df.index, df['var'], label='Variance')
    ax.set_xlabel('Email Index')
    ax.set_ylabel('Values')
    ax.set_title('Sum, Mean, and Variance of Lists')
    ax.legend()

    return df, ax