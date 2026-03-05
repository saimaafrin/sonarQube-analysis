
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Input Validation
    if not all(key in data for key in ['Salary_String', 'Experience']):
        raise ValueError("Input data missing required keys")

    # DataFrame Conversion
    df = pd.DataFrame(data)

    # Empty Data Handling
    if df.empty:
        return plt.Axes()

    # Salary Conversion
    df['Salary'] = df['Salary_String'].apply(lambda x: float(x.replace(',', '')))
    df.drop(columns=['Salary_String'], inplace=True)

    # Salary Normalization
    scaler = MinMaxScaler()
    df['Salary_Normalized'] = scaler.fit_transform(df['Salary'].values.reshape(-1, 1))

    # Data Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Salary_Normalized'])
    ax.set_xlabel('Experience')
    ax.set_ylabel('Salary')
    ax.set_title('Salary vs Experience')
    return ax