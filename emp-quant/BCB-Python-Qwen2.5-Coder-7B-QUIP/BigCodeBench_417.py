
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

    # Create a Sequential model
    model = Sequential()
    model.add(Dense(10, input_dim=2, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.01), metrics=['accuracy'])

    # Fit the model
    history = model.fit(X_train, Y_train, epochs=50, validation_data=(X_test, Y_test), verbose=0)

    # Plot the model's training and validation loss
    plt.figure()
    plt.plot(history.history['loss'], label='Train')
    plt.plot(history.history['val_loss'], label='Test')
    plt.title('Model loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Return the model and the plot's Axes object
    return model, plt.gca()