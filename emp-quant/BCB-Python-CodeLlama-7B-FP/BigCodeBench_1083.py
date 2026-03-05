import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data):
    # Input validation
    if not all(key in data for key in ['Salary_String', 'Experience']):
        raise ValueError('Input dictionary must contain keys "Salary_String" and "Experience".')

    # DataFrame conversion
    df = pd.DataFrame(data)

    # Empty data handling
    if df.empty:
        fig, ax = plt.subplots()
        ax.set_xlabel('Experience')
        ax.set_ylabel('Normalized Salary')
        return ax

    # Salary conversion
    try:
        df['Salary'] = df['Salary_String'].apply(lambda x: float(x.replace(',', '')))
    except ValueError as e:
        raise ValueError('Salary conversion failed.') from e

    # Salary normalization
    scaler = MinMaxScaler()
    df['Normalized Salary'] = scaler.fit_transform(df['Salary'].values.reshape(-1, 1))

    # Data plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Normalized Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    return ax
data = {'Salary_String': ['100000', '50000', '20000', '150000', '30000'],
        'Experience': [1, 2, 3, 4, 5]}