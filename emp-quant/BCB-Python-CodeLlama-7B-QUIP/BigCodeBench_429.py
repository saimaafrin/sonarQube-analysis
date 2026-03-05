
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns

def task_func(df1, df2):
    # Perform feature selection with SelectKBest
    selector = SelectKBest(f_classif, k=2)
    selected_features = selector.fit_transform(df1, df2)

    # Create a heatmap of the correlation between the selected features
    corr_matrix = pd.DataFrame(selected_features).corr()
    sns.heatmap(corr_matrix, annot=True, cmap="viridis")

    return selected_features, corr_matrix