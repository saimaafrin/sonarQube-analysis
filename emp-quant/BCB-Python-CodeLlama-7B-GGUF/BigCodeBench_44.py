
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(df):
    # Normalize numeric columns
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    
    # Draw box plots for each column
    fig, ax = plt.subplots()
    for col in df_scaled.columns:
        ax.boxplot(df_scaled[col])
        ax.set_title(col)
    plt.show()
    
    return df_scaled, ax