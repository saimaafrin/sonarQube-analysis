
import sqlite3
import random

def task_func(db_path,
              num_entries,
              users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)

    # Create the database and table
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            country TEXT
        )
    ''')

    # Insert random user data
    for i in range(num_entries):
        user_name = random.choice(users)
        user_age = random.randint(20, 60)
        user_country = random.choice(countries)
        c.execute('INSERT INTO users (name, age, country) VALUES (?, ?, ?)',
                  (user_name, user_age, user_country))

    conn.commit()
    conn.close()

    return db_path