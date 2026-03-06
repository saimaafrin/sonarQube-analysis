
import sqlite3
import pandas as pd
import seaborn as sns

def task_func(db_name="test.db", table_name="People"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Load data from the specified table into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # Check for negative age values
    if (df['age'] < 0).any():
        raise ValueError("Data contains negative age values.")
    
    # Close the database connection
    conn.close()
    
    # Create a Seaborn histogram with KDE
    ax = sns.histplot(df['age'], bins=30, kde=True)
    
    # Set labels for the axes
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    
    return ax