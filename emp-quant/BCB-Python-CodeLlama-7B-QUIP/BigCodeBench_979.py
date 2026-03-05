
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
    shuffled_feature_array = np.random.RandomState(seed).shuffle(feature_array)

    # Create a Pandas DataFrame from the shuffled feature array
    shuffled_feature_df = pd.DataFrame(shuffled_feature_array, columns=feature_names)

    # Create a Pandas DataFrame from the target array
    target_df = pd.DataFrame(target_array, columns=[target_name])

    # Concatenate the shuffled feature and target DataFrames
    shuffled_data = pd.concat([shuffled_feature_df, target_df], axis=1)

    # Train a Random Forest Classifier on the concatenated data
    classifier = RandomForestClassifier(random_state=seed)
    classifier.fit(shuffled_data)

    return classifier