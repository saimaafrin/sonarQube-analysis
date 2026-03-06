
import sqlite3
import random

def task_func(db_path,
              num_entries,
              users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Create the SQLite database and connect to it
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create the 'users' table
    c.execute('''CREATE TABLE users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)''')
    
    # Insert random user data into the 'users' table
    for i in range(num_entries):
        user_name = random.choice(users)
        user_age = random.randint(20, 60)
        user_country = random.choice(countries)
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (i, user_name, user_age, user_country))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    return db_path