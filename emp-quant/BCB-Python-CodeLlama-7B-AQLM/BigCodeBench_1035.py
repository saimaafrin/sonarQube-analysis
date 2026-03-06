import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    """
    Train a logistic regression model on one feature and evaluate its performance using a confusion matrix plot.
    The function takes a feature and a target series, splits them into training and testing sets, trains the logistic
    regression model, predicts the target for the test set, and plots the confusion matrix.

    Parameters:
    feature (pd.Series): Series representing the single feature for the logistic regression model.
    target (pd.Series): Series representing the target variable.

    Returns:
    (np.ndarray, plt.Axes): A tuple containing the confusion matrix and the matplotlib Axes object of the confusion matrix plot.

    Requirements:
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LogisticRegression
    - sklearn.metrics.confusion_matrix
    - numpy
    - matplotlib.pyplot

    Example:
    >>> feature = pd.Series(np.random.rand(1000)) # Feature data
    >>> target = pd.Series(np.random.randint(0, 2, size=1000)) # Target data (binary)
    >>> cm, ax = task_func(feature, target)
    >>> ax.get_title()
    'Confusion Matrix'
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.25, random_state=42)

    # Train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict the target for the test set
    y_pred = model.predict(X_test)

    # Plot the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    ax = plt.subplot()
    ax.matshow(cm)
    ax.set_title('Confusion Matrix')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.xaxis.set_label_position('center')
    ax.yaxis.set_label_position('center')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.set_xticklabels(['0', '1'])
    ax.set_yticklabels(['0', '1'])
    ax.set_xticks(np.arange(2) - 0.5, minor=False)
    ax.set_yticks(np.arange(2) - 0.5, minor=False)
    ax.grid(which='major', linestyle='-', linewidth=2)
    ax.grid(which='minor', linestyle=':', linewidth=2)
    ax.set_aspect('equal')

    return cm, ax