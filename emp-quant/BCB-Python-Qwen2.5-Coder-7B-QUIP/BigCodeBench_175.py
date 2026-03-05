
import re
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty or lacks the required columns
    if df.empty or 'Title' not in df or 'Views' not in df or 'Likes' not in df:
        return plt.subplots()

    # Filter the DataFrame to include only videos with titles containing "how" or "what"
    filtered_df = df[df['Title'].apply(lambda x: re.search(r'\b(how|what)\b', x, re.IGNORECASE))]

    # Calculate the like ratio for each video
    filtered_df['Like Ratio'] = filtered_df['Likes'] / filtered_df['Views']

    # Check if there are any matching videos
    if filtered_df.empty:
        return plt.subplots()

    # Create a bar plot of the like ratios
    fig, ax = plt.subplots()
    ax.bar(filtered_df.index, filtered_df['Like Ratio'], tick_label=filtered_df['Title'])
    ax.set_xlabel('Video Title')
    ax.set_ylabel('Like Ratio')
    ax.set_title('Like Ratios of Videos with Titles Containing "how" or "what"')

    return ax