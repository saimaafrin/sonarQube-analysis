import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(db_name="test.db", table_name="People"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Load data from the specified table into a pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # Check for negative age values
    if df['age'].min() < 0:
        raise ValueError("Data contains negative age values")
    
    # Close the database connection
    conn.close()
    
    # Create a Seaborn plot to visualize the age distribution
    ax = sns.histplot(data=df, x='age', bins=30, kde=True)
    
    # Set the title of the plot
    ax.set_title('Age Distribution')
    
    # Return the Axes object
    return ax