import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast
def task_func(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Load data from the EmailData table
    query = "SELECT email, list FROM EmailData"
    df = pd.read_sql_query(query, conn)
    
    # Convert the string representation of the list to actual list
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and variance for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    
    # Close the database connection
    conn.close()
    
    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['email'], df['sum'], label='Sum')
    ax.bar(df['email'], df['mean'], label='Mean', bottom=df['sum'])
    ax.bar(df['email'], df['var'], label='Variance', bottom=df['sum'] + df['mean'])
    ax.set_xlabel('Email')
    ax.set_ylabel('Values')
    ax.set_title('Sum, Mean, and Variance of Lists by Email')
    ax.legend()
    
    return df, ax