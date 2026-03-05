import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data):
    # Input validation
    if 'Salary_String' not in data or 'Experience' not in data:
        raise ValueError('Input dictionary must contain "Salary_String" and "Experience" keys.')

    # DataFrame conversion
    df = pd.DataFrame(data)

    # Empty data handling
    if df.empty:
        return plt.gca()

    # Salary conversion
    try:
        df['Salary'] = df['Salary_String'].apply(lambda x: float(x.replace(',', '')))
    except ValueError as e:
        raise ValueError('Salary conversion failed.') from e

    # Salary normalization
    scaler = MinMaxScaler()
    df['Salary'] = scaler.fit_transform(df['Salary'].values.reshape(-1, 1))

    # Data plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Salary')
    ax.set_title('Salary vs. Experience')
    return ax
data = {'Salary_String': ['100000', '80000', '60000', '40000', '20000'],
        'Experience': [1, 2, 3, 4, 5]}