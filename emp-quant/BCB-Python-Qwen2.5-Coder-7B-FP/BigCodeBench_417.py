from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
def task_func(X, Y):
    """
    Trains a simple neural network on given input data and target labels.
    
    Parameters:
    - X: numpy array, input data with shape (n_samples, 2)
    - Y: numpy array, target labels with shape (n_samples,)
    
    Returns:
    - Sequential: The trained Keras Sequential model.
    - matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
    
    # Construct a Sequential model
    model = Sequential([
        Dense(10, input_dim=2, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    
    # Compile the model
    optimizer = SGD(learning_rate=0.01)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    
    # Fit the model
    history = model.fit(X_train, Y_train, epochs=50, batch_size=10, verbose=0, validation_data=(X_test, Y_test))
    
    # Plot the model's training and validation loss
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['loss'], label='Train')
    plt.plot(history.history['val_loss'], label='Test')
    plt.title('Model loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
    
    return model, plt.gca()