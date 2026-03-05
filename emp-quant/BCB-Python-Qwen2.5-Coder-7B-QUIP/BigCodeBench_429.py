
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns

def task_func(df1, df2):
    # Combine the two DataFrames for feature selection
    combined_df = df1.join(df2)
    
    # Perform feature selection using SelectKBest with f_classif
    selector = SelectKBest(score_func=f_classif, k=2)
    selected_features = selector.fit_transform(combined_df)
    
    # Get the selected feature indices
    selected_indices = selector.get_support(indices=True)
    
    # Get the selected feature names
    selected_feature_names = combined_df.columns[selected_indices]
    
    # Calculate the correlation matrix for the selected features
    correlation_matrix = combined_df[selected_feature_names].corr()
    
    # Create a heatmap of the correlation matrix
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    
    # Return the selected features and the heatmap
    return selected_feature_names, heatmap