import warnings
import sklearn.model_selection as model_selection
import sklearn.svm as svm
import sklearn.datasets as datasets
import sklearn.metrics as metrics
def task_func():
    # Load the iris dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

    # Create an SVM classifier
    clf = svm.SVC(kernel='linear')

    # Train the classifier
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Calculate the accuracy of the classifier
    accuracy = metrics.accuracy_score(y_test, y_pred)

    # Check if the accuracy is less than 0.9 and set the warning message
    if accuracy < 0.9:
        warning_msg = "Warning: Accuracy is less than 0.9"
    else:
        warning_msg = None

    # Return the accuracy and warning message as a tuple
    return accuracy, warning_msg