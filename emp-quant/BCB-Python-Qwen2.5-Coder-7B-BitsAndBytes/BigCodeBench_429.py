
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df1, df2):
    # Concatenate the two dataframes
    combined_df = pd.concat([df1, df2], axis=0)
    
    # Assuming the target variable is the last column in both DataFrames
    X = combined_df.iloc[:, :-1]
    y = combined_df.iloc[:, -1]
    
    # Perform feature selection using SelectKBest with k=2
    selector = SelectKBest(f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    
    # Get the indices of the selected features
    selected_indices = selector.get_support(indices=True)
    
    # Get the names of the selected features
    selected_features = X.columns[selected_indices].tolist()
    
    # Calculate the correlation matrix for the selected features
    corr_matrix = X_new.T.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap of Selected Features')
    plt.show()
    
    # Return the selected features and the heatmap axes
    return selected_features, plt.gca()