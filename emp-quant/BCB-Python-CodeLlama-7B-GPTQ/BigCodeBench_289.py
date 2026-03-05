import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
def task_func(X, y, n_splits, batch_size, epochs):
    # Initialize the scaler
    scaler = MinMaxScaler()

    # Scale the data
    X_scaled = scaler.fit_transform(X)

    # Initialize the model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(20, activation='relu', input_shape=(X.shape[1],)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Initialize the k-fold object
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    # Initialize the list to store the training histories
    histories = []

    # Iterate over the folds
    for train_index, val_index in kf.split(X_scaled):
        # Split the data
        X_train, X_val = X_scaled[train_index], X_scaled[val_index]
        y_train, y_val = y[train_index], y[val_index]

        # Train the model
        history = model.fit(X_train, y_train,
                            batch_size=batch_size,
                            epochs=epochs,
                            validation_data=(X_val, y_val))

        # Append the training history to the list
        histories.append(history)

    # Return the list of training histories
    return histories
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 1, 1, 0]
n_splits = 3
batch_size = 32
epochs = 10