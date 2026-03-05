import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    # Check if df is a DataFrame and contains the 'Letters' column
    if not isinstance(df, pd.DataFrame) or 'Letters' not in df.columns:
        raise ValueError("Input must be a DataFrame with a 'Letters' column")
    
    # Count the frequency of each letter in the 'Letters' column
    letter_counts = df['Letters'].value_counts()
    
    # Create a bar chart of the letter frequencies
    fig, ax = plt.subplots()
    ax.bar(letter_counts.index, letter_counts.values)
    
    # Set the labels and title for the bar chart
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Letter Frequency')
    
    return ax