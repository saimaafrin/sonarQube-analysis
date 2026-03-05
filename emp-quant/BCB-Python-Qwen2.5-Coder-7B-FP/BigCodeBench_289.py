import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
def task_func(X, y, n_splits, batch_size, epochs):
    # Normalize the data
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Initialize the KFold cross-validator
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    # Initialize a list to store the training history for each fold
    histories = []
    
    # Iterate over each fold
    for train_index, test_index in kf.split(X_scaled):
        X_train, X_test = X_scaled[train_index], X_scaled[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        # Define the model
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(20, activation='relu', input_shape=(X_train.shape[1],)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        # Compile the model
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        # Train the model
        history = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_test, y_test))
        
        # Append the history to the list
        histories.append(history.history)
    
    return histories