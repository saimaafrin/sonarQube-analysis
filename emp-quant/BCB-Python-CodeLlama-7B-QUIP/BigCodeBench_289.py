
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

def task_func(X, y, n_splits, batch_size, epochs):
    # Normalize the data
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    y = scaler.fit_transform(y)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Define the model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(20, activation='relu', input_shape=(n_features,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Define the k-fold cross-validation
    kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    # Define the training and testing functions
    def train_func(model, X, y):
        return model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=0)

    def test_func(model, X, y):
        return model.evaluate(X, y)

    # Perform the k-fold cross-validation
    histories = []
    for train_index, test_index in kfold.split(X_train):
        # Get the training and testing data for this fold
        X_train_fold = X_train[train_index]
        y_train_fold = y_train[train_index]
        X_test_fold = X_test[test_index]
        y_test_fold = y_test[test_index]

        # Train the model on the training data
        model.fit(X_train_fold, y_train_fold, epochs=epochs, batch_size=batch_size, verbose=0)

        # Evaluate the model on the testing data
        history = model.evaluate(X_test_fold, y_test_fold)
        histories.append(history)

    return histories