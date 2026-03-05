import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
def task_func(df, freq='D', decomposition_model='multiplicative'):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'value' column exists in the DataFrame
    if 'value' not in df.columns:
        raise ValueError("DataFrame must contain a 'value' column.")
    
    # Check if 'value' column contains valid numeric data
    if not pd.api.types.is_numeric_dtype(df['value']):
        raise ValueError("The 'value' column must contain numeric data.")
    
    # Check if 'freq' is a valid frequency string
    valid_freqs = ['D', 'W', 'M', 'Q', 'A', 'H', 'T', 'S']
    if freq not in valid_freqs:
        raise ValueError("Invalid frequency string. Choose from: 'D', 'W', 'M', 'Q', 'A', 'H', 'T', 'S'.")
    
    # Check if 'decomposition_model' is either 'additive' or 'multiplicative'
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("Invalid decomposition model. Choose from: 'additive' or 'multiplicative'.")
    
    # Perform the decomposition
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, period=freq)
    
    # Plot the decomposition
    fig, axes = plt.subplots(4, 1, figsize=(10, 8))
    decomposition.plot(ax=axes)
    plt.tight_layout()
    
    return decomposition, axes