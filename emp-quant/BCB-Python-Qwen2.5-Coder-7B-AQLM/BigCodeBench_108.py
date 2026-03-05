
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(df, freq='D', decomposition_model='multiplicative'):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame")
    
    # Check if 'value' column exists
    if 'value' not in df.columns:
        raise ValueError("df must contain a 'value' column")
    
    # Check if 'value' column contains valid data type
    if not pd.api.types.is_numeric_dtype(df['value']):
        raise ValueError("The 'value' column must contain numeric data")
    
    # Check if 'freq' is a valid frequency string
    valid_freqs = ['D', 'W', 'M', 'Q', 'A', 'H', 'T', 'S']
    if freq not in valid_freqs:
        raise ValueError(f"Invalid frequency '{freq}'. Valid frequencies are: {', '.join(valid_freqs)}")
    
    # Check if 'decomposition_model' is either 'additive' or 'multiplicative'
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError(f"Invalid decomposition model '{decomposition_model}'. Valid models are: 'additive' or 'multiplicative'")
    
    # Perform decomposition
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, period=12 if freq in ['M', 'Q', 'A'] else 1)
    
    # Plot the decomposition
    fig, axes = plt.subplots(4, 1, figsize=(10, 10))
    decomposition.plot(ax=axes)
    plt.tight_layout()
    
    return decomposition, axes