
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(X, y, n_splits, batch_size, epochs):
    # Normalize the data
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Initialize the KFold cross-validator
    kf = KFold(n_splits=n_splits, shuffle=True)

    # Initialize a list to store the training history for each fold
    fold_histories = []

    # Define the model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Perform k-fold cross-validation
    for fold in range(n_splits):
        # Split the data into training and validation sets
        indices = np.random.permutation(X.shape[0])
        X_train, X_val = X[indices], X[indices]
        y_train, y_val = y[indices], y[indices]

        # Train the model
        history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size, verbose=0)

        # Append the training history to the list
        fold_histories.append(history)

    return fold_histories