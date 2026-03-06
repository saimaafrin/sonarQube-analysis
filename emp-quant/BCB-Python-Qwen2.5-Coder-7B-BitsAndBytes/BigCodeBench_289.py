
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

def task_func(X, y, n_splits, batch_size, epochs):
    # Normalize the input features
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Initialize the KFold cross-validator
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    histories = []
    
    for train_index, val_index in kf.split(X_scaled):
        X_train, X_val = X_scaled[train_index], X_scaled[val_index]
        y_train, y_val = y[train_index], y[val_index]
        
        # Define the model architecture
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(20, activation='relu', input_shape=(X.shape[1],)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        # Compile the model
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        # Train the model
        history = model.fit(X_train, y_train, validation_data=(X_val, y_val), batch_size=batch_size, epochs=epochs)
        
        # Append the history to the list
        histories.append(history.history)
    
    return histories