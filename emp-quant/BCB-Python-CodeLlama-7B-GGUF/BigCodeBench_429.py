
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns

def task_func(df1, df2):
    # Perform feature selection with SelectKBest
    selector = SelectKBest(k=2)
    selector.fit(df1, df2)
    selected_features = selector.get_support(indices=True)

    # Create a heatmap of the correlation between the selected features
    corr_matrix = df1.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

    return selected_features, corr_matrix