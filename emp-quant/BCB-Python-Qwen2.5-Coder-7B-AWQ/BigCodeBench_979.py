import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    """
    Shuffles the columns of a given numpy array and trains a Random Forest Classifier on the shuffled data.
    
    Parameters:
    - feature_array: numpy array, the feature data.
    - target_array: numpy array, the target data.
    - feature_names: list of str, the names of the feature columns.
    - target_name: str, the name of the target column.
    - seed: int, the random seed for reproducibility.
    
    Returns:
    - sklearn.ensemble.RandomForestClassifier: A trained Random Forest Classifier on the shuffled feature data.
    """
    # Ensure the input arrays are numpy arrays
    feature_array = np.array(feature_array)
    target_array = np.array(target_array)
    
    # Shuffle the columns of the feature array
    np.random.seed(seed)
    shuffled_indices = np.random.permutation(feature_array.shape[1])
    shuffled_feature_array = feature_array[:, shuffled_indices]
    
    # Create a DataFrame for the shuffled feature array
    shuffled_df = pd.DataFrame(shuffled_feature_array, columns=[feature_names[i] for i in shuffled_indices])
    
    # Add the target column to the DataFrame
    shuffled_df[target_name] = target_array
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(shuffled_df.drop(target_name, axis=1), shuffled_df[target_name], test_size=0.2, random_state=seed)
    
    # Initialize and train the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=seed)
    rf_classifier.fit(X_train, y_train)
    
    return rf_classifier