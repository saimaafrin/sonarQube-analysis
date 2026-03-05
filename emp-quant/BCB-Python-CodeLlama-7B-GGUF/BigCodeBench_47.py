
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Standardize numeric columns
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    
    # Replace missing values with column means
    df_scaled = df_scaled.fillna(df_scaled.mean())
    
    # Create correlation matrix
    corr_matrix = df_scaled.corr()
    
    # Plot heatmap
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.show()
    
    return df_scaled, corr_matrix