from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    # Standardize numeric columns
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df)

    # Replace missing values with column means
    df_std = df_std.fillna(df_std.mean())

    # Compute correlation matrix
    corr = df_std.corr()

    # Plot heatmap of correlation matrix
    sns.heatmap(corr, annot=True, cmap="coolwarm")

    # Return DataFrame and heatmap
    return df_std, corr
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10], "C": [11, 12, 13, 14, 15]})