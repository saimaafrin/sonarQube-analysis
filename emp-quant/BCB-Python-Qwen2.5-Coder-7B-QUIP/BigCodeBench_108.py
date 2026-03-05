
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(df, freq='D', decomposition_model='multiplicative'):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame")
    
    # Check if 'value' column exists in df
    if 'value' not in df:
        raise ValueError("df must contain a 'value' column")
    
    # Check if 'value' column contains valid data types
    if not df['value'].dtype in [pd.api.types.CategoricalDtype, pd.api.types.CategoricalDtype]:
        raise ValueError("df['value'] must be of a numeric data type")
    
    # Check if freq is a valid frequency string
    if freq not in ['D', 'W', 'M', 'Q', 'A']:
        raise ValueError("freq must be a valid frequency string")
    
    # Check if decomposition_model is 'additive' or 'multiplicative'
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("decomposition_model must be 'additive' or 'multiplicative'")
    
    # Perform the decomposition
    result = seasonal_decompose(df['value'], model=decomposition_model, two_sided=True, periods=365)
    
    # Plot the decomposition
    fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
    axes[0].plot(result.trend, label='Trend')
    axes[0].set_title('Trend')
    axes[1].plot(result.seasonal, label='Seasonal')
    axes[1].set_title('Seasonal')
    axes[2].plot(result.resid, label='Residuals')
    axes[2].set_title('Residuals')
    axes[3].plot(result.fittedvalue, label='Fitted Value')
    axes[3].set_title('Fitted Value')
    
    # Return the decomposition result and the matplotlib Axes object
    return result, axes