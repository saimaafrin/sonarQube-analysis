
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df1, df2):
    # Concatenate the two dataframes
    combined_df = pd.concat([df1, df2], axis=0)
    
    # Perform feature selection with SelectKBest (k=2)
    X = combined_df.drop('target', axis=1)  # Assuming 'target' is the column to predict
    y = combined_df['target']
    selector = SelectKBest(f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    
    # Get the selected feature names
    selected_features = X.columns[selector.get_support()]
    
    # Create a heatmap of the correlation between the selected features
    correlation_matrix = X_new.T.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap of Selected Features')
    plt.show()
    
    # Return the selected features and the heatmap
    return selected_features, plt.gca()