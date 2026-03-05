import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
def task_func(df1, df2):
    # Perform feature selection with SelectKBest
    selector = SelectKBest(k=2)
    selector.fit(df1, df2)
    selected_features = selector.get_support(indices=True)

    # Create a heatmap of the feature correlations
    corr_matrix = df1.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

    return selected_features, corr_matrix
df1 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10], "C": [11, 12, 13, 14, 15]})
df2 = pd.DataFrame({"A": [16, 17, 18, 19, 20], "B": [21, 22, 23, 24, 25], "C": [26, 27, 28, 29, 30]})