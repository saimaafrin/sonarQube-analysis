
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
    # Create a DataFrame from the feature array and target array
    df = pd.DataFrame(feature_array, columns=feature_names)
    df[target_name] = target_array
    
    # Shuffle the columns of the DataFrame
    if seed is not None:
        np.random.seed(seed)
    shuffled_columns = df.columns.tolist()
    np.random.shuffle(shuffled_columns)
    df = df[shuffled_columns]
    
    # Split the shuffled DataFrame back into features and target
    X_shuffled = df.drop(target_name, axis=1).values
    y_shuffled = df[target_name].values
    
    # Train a Random Forest Classifier on the shuffled data
    clf = RandomForestClassifier(random_state=seed)
    clf.fit(X_shuffled, y_shuffled)
    
    return clf