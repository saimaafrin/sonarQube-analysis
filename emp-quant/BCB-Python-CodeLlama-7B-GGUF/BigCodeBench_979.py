
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
    
    # Create a pandas DataFrame from the shuffled feature array
    feature_df = pd.DataFrame(feature_array, columns=feature_names)
    
    # Create a pandas Series from the target array
    target_series = pd.Series(target_array, name=target_name)
    
    # Concatenate the feature and target arrays into a single DataFrame
    data = pd.concat([feature_df, target_series], axis=1)
    
    # Split the data into training and testing sets
    train_data, test_data = data.split(test_size=0.2, random_state=seed)
    
    # Train a Random Forest Classifier on the training data
    clf = RandomForestClassifier(n_estimators=100, random_state=seed)
    clf.fit(train_data.drop(target_name, axis=1), train_data[target_name])
    
    # Return the trained Random Forest Classifier
    return clf