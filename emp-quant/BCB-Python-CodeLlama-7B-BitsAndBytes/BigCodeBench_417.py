
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

    # Define the model
    model = Sequential()
    model.add(Dense(units=64, activation='sigmoid', input_shape=(2,)))
    model.add(Dense(units=1))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.01), metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train, Y_train, epochs=100, verbose=0)

    # Plot the training and validation loss
    plt.plot(history.history['loss'], label='Train')
    plt.plot(history.history['val_loss'], label='Test')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Model loss')
    plt.legend()

    # Return the Axes object
    return plt.gca()

# Generate some random data
X = np.random.rand(100, 2)
Y = np.random.randint(0, 2, 100)

# Run the task function
ax = task_func(X, Y)

# Show the plot
plt.show()