from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(df):
    # Normalize numeric columns
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Draw box plots for each column
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in df_scaled.columns:
        ax.boxplot(df_scaled[col])
        ax.set_title(f"Box plot for {col}")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.set_xticklabels(df_scaled[col])

    return df_scaled, ax
df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50],
    "C": [100, 200, 300, 400, 500],
    "D": [1000, 2000, 3000, 4000, 5000],
})