
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Replace missing values with the mean of each column
    df.fillna(df.mean(), inplace=True)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the numeric columns
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    # Calculate the correlation matrix
    corr_matrix = df_scaled.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df_scaled, plt.gca()