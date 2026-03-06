import warnings
import sklearn.model_selection as model_selection
import sklearn.svm as svm
import sklearn.datasets as datasets
import sklearn.metrics as metrics
def task_func():
    """
    Perform an SVM classification of the iris dataset and warn if the accuracy is less than 0.9.
    The warning action is set to 'always'. The test size for the train-test split is 0.33.

    Parameters:
    - None

    Returns:
    tuple: A tuple containing:
        - accuracy (float): The accuracy of the SVM classification.
        - warning_msg (str or None): A warning message if the accuracy is below 0.9, None otherwise.

    Requirements:
    - warnings
    - sklearn

    Example:
    >>> task_func()
    (1.0, None)
    """
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)
    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    if accuracy < 0.9:
        warning_msg = 'The accuracy of the SVM classification is less than 0.9.'
        warnings.warn(warning_msg, Warning, stacklevel=2)
    else:
        warning_msg = None
    return accuracy, warning_msg