
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Replace missing values with the column's average
    df = df.fillna(df.mean())

    # Standardize the DataFrame
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df)

    # Create a heatmap of the correlation matrix
    corr_matrix = df_std.corr().round(1)
    ax = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.show()

    return df_std, ax