
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Input Validation
    if 'Salary_String' not in data or 'Experience' not in data:
        raise ValueError("Input dictionary must contain 'Salary_String' and 'Experience' keys")

    # DataFrame Conversion
    df = pd.DataFrame(data)

    # Empty Data Handling
    if df.empty:
        return plt.Axes(xlabel='Experience', ylabel='Normalized Salary')

    # Salary Conversion
    try:
        df['Salary'] = df['Salary_String'].apply(lambda x: float(x.replace(',', '')))
    except ValueError:
        raise ValueError("Salary conversion failed. Check input data for errors.")

    # Salary Normalization
    scaler = MinMaxScaler()
    df['Normalized Salary'] = scaler.fit_transform(df['Salary'].values.reshape(-1, 1))

    # Data Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Normalized Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    return ax