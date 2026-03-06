import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
def task_func(X, y, n_splits, batch_size, epochs):
    """
    Trains a simple neural network on provided data using k-fold cross-validation.
    The network has one hidden layer with 20 neurons and ReLU activation, and
    an output layer with sigmoid activation for binary classification.

    Parameters:
        X (numpy.array): The input data.
        y (numpy.array): The target data.
        n_splits (int): The number of splits for k-fold cross-validation. Default is 5.
        batch_size (int): The size of the batch used during training. Default is 32.
        epochs (int): The number of epochs for training the model. Default is 1.

    Returns:
        list: A list containing the training history of the model for each fold. Each history
              object includes training loss and accuracy.

    Requirements:
    - tensorflow
    - sklearn.model_selection.KFold
    - sklearn.preprocessing.MinMaxScaler

    Examples:
    >>> import numpy as np
    >>> X = np.random.rand(100, 10)
    >>> y = np.random.randint(0, 2, 100)
    >>> history = task_func(X, y, 5, 32, 1)
    >>> isinstance(history, list)
    True
    >>> len(history)
    5
    >>> all('loss' in hist.history.keys() for hist in history)
    True
    """
    # Create a scaler for the input data
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Create a k-fold cross-validation object
    kf = KFold(n_splits=n_splits)

    # Create a list to store the training histories
    histories = []

    # Iterate over the folds
    for train_index, test_index in kf.split(X):
        # Split the data
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Create the model
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(20, activation='relu', input_shape=(X_train.shape[1],)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compile the model
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        # Train the model
        history = model.fit(X_train, y_train,
                            batch_size=batch_size,
                            epochs=epochs,
                            verbose=0,
                            validation_data=(X_test, y_test))

        # Append the training history to the list
        histories.append(history)

    return histories