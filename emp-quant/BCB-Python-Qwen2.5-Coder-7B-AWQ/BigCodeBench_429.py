import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df1, df2):
    # Concatenate the two dataframes
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    # Perform feature selection with SelectKBest
    X = combined_df.drop('target', axis=1)  # Assuming 'target' is the column to predict
    y = combined_df['target']
    selector = SelectKBest(f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    
    # Get the selected feature indices
    selected_indices = selector.get_support(indices=True)
    
    # Get the names of the selected features
    selected_features = X.columns[selected_indices].tolist()
    
    # Create a heatmap of the correlation between the selected features
    correlation_matrix = X[selected_features].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.show()
    
    # Return the selected features and the heatmap
    return selected_features, plt