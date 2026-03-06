
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
    ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.set_title('Confusion Matrix')
    tick_marks = np.arange(len(np.unique(target)))
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xlabel('Predicted label')
    ax.set_ylabel('True label')
    
    # Annotate the confusion matrix
    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in np.ndindex(cm.shape):
        ax.text(j, i, format(cm[i, j], fmt),
                horizontalalignment="center",
                color="white" if cm[i, j] > thresh else "black")
    
    return cm, ax