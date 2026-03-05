
import sqlite3
from random import choice, seed
import os

def task_func(db_name, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative")
    
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 66)
    HEIGHTS = range(150, 201)
    
    if random_seed is not None:
        seed(random_seed)
    
    # Create the database and table
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")
    
    # Insert random data into the table
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cursor.execute(f"INSERT INTO {table_name} (name, age, height) VALUES (?, ?, ?)", (name, age, height))
    
    conn.commit()
    conn.close()
    
    return os.path.abspath(db_name)