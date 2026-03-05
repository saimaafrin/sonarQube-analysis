import sqlite3
import numpy as np
from random import choice, seed
NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
AGES = range(18, 65)
HEIGHTS = range(150, 200)
def task_func(db_path, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative")
    
    seed(random_seed)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it does not exist
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            height INTEGER NOT NULL
        )
    ''')
    
    # Insert random data into the table
    for _ in range(num_entries):
        name = choice(NAMES)
        age = np.random.choice(list(AGES))
        height = np.random.choice(list(HEIGHTS))
        cursor.execute(f'''
            INSERT INTO {table_name} (name, age, height) VALUES (?, ?, ?)
        ''', (name, age, height))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Return the number of rows inserted
    return num_entries