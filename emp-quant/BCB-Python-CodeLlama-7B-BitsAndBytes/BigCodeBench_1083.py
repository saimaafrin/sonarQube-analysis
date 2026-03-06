
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Input validation
    if 'Salary_String' not in data or 'Experience' not in data:
        raise ValueError("Input dictionary must contain 'Salary_String' and 'Experience' keys")

    # DataFrame conversion
    df = pd.DataFrame(data)

    # Empty data handling
    if df.empty:
        return plt.Axes(figsize=(8, 6), facecolor='w', edgecolor='k')

    # Salary conversion
    try:
        df['Salary'] = df['Salary_String'].apply(lambda x: float(x.replace(',', '')))
    except ValueError:
        raise ValueError("Salary conversion failed")

    # Salary normalization
    scaler = MinMaxScaler()
    df['Normalized_Salary'] = scaler.fit_transform(df['Salary'].values.reshape(-1, 1))

    # Data plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df['Experience'], df['Normalized_Salary'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    ax.set_title('Salary vs. Experience')
    return ax