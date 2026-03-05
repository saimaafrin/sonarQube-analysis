import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    """
    Train a logistic regression model on one feature and evaluate its performance using a confusion matrix plot.
    The function takes a feature and a target series, splits them into training and testing sets, trains the logistic regression model, predicts the target for the test set, and plots the confusion matrix.
    The function should output with:
        (np.ndarray, plt.Axes): A tuple containing the confusion matrix and the matplotlib Axes object of the confusion matrix plot.
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=42)

    # Train a logistic regression model on the training data
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict the target for the test set
    y_pred = model.predict(X_test)

    # Create a confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot the confusion matrix
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, ax=ax, cmap="Blues")
    ax.set_xlabel("Predicted label")
    ax.set_ylabel("True label")
    ax.set_title("Confusion Matrix")

    return cm, ax
feature = pd.Series([1, 2, 3, 4, 5])
target = pd.Series([0, 1, 1, 0, 1])