import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data):
    # Input Validation
    if not all(key in data for key in ['Salary_String', 'Experience']):
        raise ValueError('The input dictionary must contain the keys "Salary_String" and "Experience".')

    # DataFrame Conversion
    df = pd.DataFrame(data)

    # Empty Data Handling
    if df.empty:
        fig, ax = plt.subplots()
        ax.set_xlabel('Experience')
        ax.set_ylabel('Normalized Salary')
        return ax

    # Salary Conversion
    try:
        df['Salary'] = df['Salary_String'].apply(lambda x: float(x.replace(',', '')))
    except ValueError as e:
        raise ValueError('Salary conversion failed.') from e

    # Salary Normalization
    scaler = MinMaxScaler()
    df['Normalized Salary'] = scaler.fit_transform(df['Salary'].values.reshape(-1, 1))

    # Data Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Normalized Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    return ax
data = {'Salary_String': ['100000', '200000', '300000', '400000', '500000'],
        'Experience': [1, 2, 3, 4, 5]}