import sqlite3
import pandas as pd
def task_func(db_name, table_name):
    """
    Plot the relationship between the first and second numerical columns of an SQLite3 table, after excluding 'id' column.

    Parameters:
    - db_name (str): The absolute path to the SQLite3 database.
    - table_name (str): The name of the table to plot from.

    Returns:
    - matplotlib.axes._axes.Axes: Scatterplot with column name labeled on their respective axes.

    Raises:
    - ValueError: If the table has less than two numerical columns.
    
    Requirements:
    - sqlite3
    - pandas

    Example:
    >>> ax = task_func('/path/to/database/test.db', 'People')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0.9400000000000001, 0, '0.94'), ... ]
    """
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
    conn.close()
    if len(df.select_dtypes(include=['number']).columns) < 2:
        raise ValueError('Table must have at least two numerical columns.')
    ax = df.drop('id', axis=1).plot.scatter(x=df.select_dtypes(include=['number']).columns[0], y=df.select_dtypes(include=['number']).columns[1], figsize=(10, 10))
    ax.set_xlabel(df.select_dtypes(include=['number']).columns[0])
    ax.set_ylabel(df.select_dtypes(include=['number']).columns[1])
    return ax