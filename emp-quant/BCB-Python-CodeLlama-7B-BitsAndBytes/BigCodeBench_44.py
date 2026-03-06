
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(df):
    # Normalize numeric columns
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Replace missing values with column average
    df_scaled = df_scaled.fillna(df_scaled.mean())

    # Draw box plot for each column
    fig, axs = plt.subplots(ncols=len(df_scaled.columns), figsize=(12, 6))
    for i, col in enumerate(df_scaled.columns):
        axs[i].boxplot(df_scaled[col])
        axs[i].set_title(f"Box Plot for {col}")
        axs[i].set_xlabel("Value")
        axs[i].set_ylabel("Frequency")

    return df_scaled, axs