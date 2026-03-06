
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    # Shuffle the columns of the feature array
    feature_array = np.random.permutation(feature_array)

    # Create a Pandas DataFrame from the feature and target arrays
    df = pd.DataFrame(feature_array, columns=feature_names)
    df[target_name] = target_array

    # Train a Random Forest Classifier on the shuffled data
    clf = RandomForestClassifier(n_estimators=100, random_state=seed)
    clf.fit(df.drop(target_name, axis=1), df[target_name])

    return clf

clf = task_func(feature_array, target_array, seed=42)
print(clf)