
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
    # Ensure the feature and target arrays are numpy arrays
    feature_array = np.array(feature_array)
    target_array = np.array(target_array)
    
    # Shuffle the columns of the feature array
    np.random.seed(seed)
    shuffled_indices = np.random.permutation(feature_array.shape[1])
    shuffled_feature_array = feature_array[:, shuffled_indices]
    
    # Create a DataFrame for the shuffled feature array
    shuffled_feature_df = pd.DataFrame(shuffled_feature_array, columns=feature_names)
    
    # Create a DataFrame for the target array
    target_df = pd.DataFrame(target_array, columns=[target_name])
    
    # Combine the shuffled feature and target DataFrames
    combined_df = pd.concat([shuffled_feature_df, target_df], axis=1)
    
    # Split the combined DataFrame into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        combined_df[feature_names], combined_df[target_name], test_size=0.2, random_state=seed
    )
    
    # Initialize and train the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=seed)
    rf_classifier.fit(X_train, y_train)
    
    return rf_classifier