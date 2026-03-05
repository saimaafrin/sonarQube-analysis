
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df1, df2):
    # Concatenate the two dataframes
    combined_df = pd.concat([df1, df2], axis=1)
    
    # Select the target variable
    y = combined_df['target']
    X = combined_df.drop('target', axis=1)
    
    # Perform feature selection with SelectKBest
    selector = SelectKBest(score_func=f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    
    # Get the selected feature names
    selected_features = X.columns[selector.get_support()]
    
    # Calculate the correlation matrix for the selected features
    corr_matrix = X_new.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap of Selected Features')
    plt.show()
    
    # Return the selected features and the heatmap
    return selected_features, plt