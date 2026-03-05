
import sqlite3
import numpy as np
from random import choice, seed

NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
AGES = range(18, 65)
HEIGHTS = range(150, 200)

def task_func(db_path, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative")
    
    if random_seed is not None:
        seed(random_seed)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it does not exist
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            height INTEGER
        )
    ''')
    
    # Insert random data
    for _ in range(num_entries):
        name = choice(NAMES)
        age = np.random.choice(list(AGES))
        height = np.random.choice(list(HEIGHTS))
        cursor.execute(f'''
            INSERT INTO {table_name} (name, age, height) VALUES (?, ?, ?)
        ''', (name, age, height))
    
    conn.commit()
    conn.close()
    
    return num_entries