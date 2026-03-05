
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Step 1: Input Validation
    if 'Salary_String' not in data or 'Experience' not in data:
        raise ValueError("Input dictionary must contain 'Salary_String' and 'Experience' keys.")
    
    # Step 2: DataFrame Conversion
    df = pd.DataFrame(data)
    
    # Step 3: Empty Data Handling
    if df.empty:
        return plt.subplots()
    
    # Step 4: Salary Conversion
    try:
        df['Salary'] = df['Salary_String'].str.replace(',', '').astype(float)
    except ValueError as e:
        raise ValueError("Failed to convert 'Salary_String' to float.") from e
    
    # Step 5: Salary Normalization
    scaler = MinMaxScaler()
    df['Normalized_Salary'] = scaler.fit_transform(df[['Salary']])
    
    # Step 6: Data Plotting
    fig, ax = plt.subplots()
    ax.scatter(df['Experience'], df['Normalized_Salary'], c='blue', marker='o')
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    
    return ax