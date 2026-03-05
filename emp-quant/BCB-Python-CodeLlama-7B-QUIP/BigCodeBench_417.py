
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, shuffle=True)

    # Define the model
    model = Sequential()
    model.add(Dense(units=1, input_shape=(2,), activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.01))

    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=100, verbose=0)

    # Evaluate the model on the test data
    test_loss = model.evaluate(X_test, Y_test)

    # Plot the training and validation loss over epochs
    plt.figure(figsize=(8, 6))
    plt.plot(range(100), model.history['loss'], label='Train')
    plt.plot(range(100), model.history['val_loss'], label='Test')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Model loss')
    plt.show()

    return model, plt.gca()