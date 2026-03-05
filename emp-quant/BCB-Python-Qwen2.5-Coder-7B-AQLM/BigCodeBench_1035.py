
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(feature.values.reshape(-1, 1), target.values, test_size=0.2, random_state=42)
    
    # Initialize and train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Predict the target for the test set
    y_pred = model.predict(X_test)
    
    # Calculate the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Plot the confusion matrix
    fig, ax = plt.subplots()
    ax.matshow(cm, cmap='Blues')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    plt.show()
    
    return cm, ax