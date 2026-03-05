import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data):
    # Step 1: Input Validation
    required_keys = ['Salary_String', 'Experience']
    if not all(key in data for key in required_keys):
        raise ValueError("Input dictionary must contain 'Salary_String' and 'Experience' keys.")
    
    # Step 2: DataFrame Conversion
    df = pd.DataFrame(data)
    
    # Step 3: Empty Data Handling
    if df.empty:
        return plt.gca()  # Return an Axes instance with labeled axes but no data
    
    # Step 4: Salary Conversion
    try:
        df['Salary'] = df['Salary_String'].str.replace(',', '').astype(float)
    except ValueError as e:
        raise ValueError("Failed to convert 'Salary_String' to float.") from e
    
    # Step 5: Salary Normalization
    scaler = MinMaxScaler()
    df['Normalized_Salary'] = scaler.fit_transform(df[['Salary']])
    
    # Step 6: Data Plotting
    ax = df.plot(kind='scatter', x='Experience', y='Normalized_Salary', figsize=(10, 6))
    ax.set_xlabel('Experience')
    ax.set_ylabel('Normalized Salary')
    ax.set_title('Normalized Salary vs Experience')
    
    return ax