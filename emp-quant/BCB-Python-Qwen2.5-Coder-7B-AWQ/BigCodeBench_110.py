import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'Date' and 'Sales' columns exist in the DataFrame
    required_columns = ['Date', 'Sales']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Input 'df' must contain the following columns: {', '.join(required_columns)}. Missing columns: {', '.join(missing_columns)}")
    
    # Check if the DataFrame has data to plot
    if df.empty:
        raise ValueError("Input 'df' must contain data to plot.")
    
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set 'Date' column as the index
    df.set_index('Date', inplace=True)
    
    # Create the line chart
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Daily Turnover Line Chart')
    
    return ax