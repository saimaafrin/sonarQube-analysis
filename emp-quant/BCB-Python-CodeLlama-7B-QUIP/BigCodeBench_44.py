
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(df):
    # Normalize numeric columns
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Create a figure and axis for each column
    fig, axes = plt.subplots(nrows=df.shape[1], ncols=1, figsize=(10, 10))

    # Draw a box plot for each column
    for i, col in enumerate(df_scaled.columns):
        axes[i].boxplot(df_scaled[col])
        axes[i].set_title(f"{col} normalized")

    # Show the figure
    plt.show()

    return df_scaled