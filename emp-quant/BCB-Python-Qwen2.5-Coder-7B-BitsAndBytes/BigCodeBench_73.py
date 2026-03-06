
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
    
    # Convert the string representation of lists to actual lists
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and variance for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    
    # Close the database connection
    conn.close()
    
    # Plotting the results
    fig, ax = plt.subplots()
    df[['sum', 'mean', 'var']].plot(kind='bar', ax=ax)
    ax.set_xlabel('Email')
    ax.set_ylabel('Values')
    ax.set_title('Sum, Mean, and Variance of Lists per Email')
    
    return df, ax