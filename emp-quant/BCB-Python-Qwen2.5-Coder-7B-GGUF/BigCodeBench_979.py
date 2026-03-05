
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
    # Ensure the input arrays are numpy arrays
    feature_array = np.array(feature_array)
    target_array = np.array(target_array)
    
    # Create a DataFrame from the feature array with column names
    df = pd.DataFrame(feature_array, columns=feature_names)
    
    # Shuffle the columns of the DataFrame
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    
    # Split the shuffled DataFrame back into feature and target arrays
    shuffled_feature_array = df.values
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        shuffled_feature_array, target_array, test_size=0.2, random_state=seed
    )
    
    # Initialize and train the Random Forest Classifier
    clf = RandomForestClassifier(random_state=seed)
    clf.fit(X_train, y_train)
    
    return clf