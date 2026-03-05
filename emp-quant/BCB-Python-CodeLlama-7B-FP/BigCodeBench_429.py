import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
def task_func(df1, df2):
    # Perform feature selection with SelectKBest
    selector = SelectKBest(k=2)
    X = selector.fit_transform(df1, df2)

    # Create a heatmap of the feature correlations
    sns.heatmap(X.corr(), annot=True, cmap="coolwarm")

    # Return a tuple containing the selected features and the heatmap
    return (selector.get_support(indices=True), sns.heatmap)
df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
df2 = pd.DataFrame({"A": [10, 20, 30], "B": [40, 50, 60], "C": [70, 80, 90]})