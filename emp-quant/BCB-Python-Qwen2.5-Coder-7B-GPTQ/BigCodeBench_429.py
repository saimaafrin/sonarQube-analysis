import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df1, df2):
    # Concatenate the two dataframes
    combined_df = pd.concat([df1, df2], axis=1)
    
    # Perform feature selection with SelectKBest
    selector = SelectKBest(f_classif, k=2)
    X = combined_df.drop('target', axis=1)  # Assuming 'target' is the column to predict
    y = combined_df['target']
    selector.fit(X, y)
    
    # Get the mask of selected features
    selected_features_mask = selector.get_support()
    
    # Get the list of selected features
    selected_features = X.columns[selected_features_mask].tolist()
    
    # Calculate the correlation matrix for the selected features
    correlation_matrix = X[selected_features].corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap of Selected Features')
    plt.show()
    
    # Return the selected features and the heatmap
    return selected_features, plt.gca()