
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    # Shuffle the columns of the feature array
    np.random.seed(seed)
    shuffled_feature_array = np.random.permutation(feature_array.T).T

    # Create a DataFrame with the shuffled feature data
    df = pd.DataFrame(shuffled_feature_array, columns=feature_names)

    # Add the target column to the DataFrame
    df[target_name] = target_array

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        df[feature_names], df[target_name], test_size=0.2, random_state=seed
    )

    # Initialize and train the Random Forest Classifier
    classifier = RandomForestClassifier(n_estimators=100, random_state=seed)
    classifier.fit(X_train, y_train)

    # Evaluate the classifier on the test set
    y_pred = classifier.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    return classifier