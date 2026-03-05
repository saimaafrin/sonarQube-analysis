from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt
def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Construct a Keras Sequential model with one hidden dense layer and sigmoid activation
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(64, activation='sigmoid', input_shape=(X.shape[1],)))

    # Compile the model with binary cross-entropy loss and SGD optimizer
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

    # Fit the model to the training data in a non-verbose mode
    model.fit(X_train, Y_train, epochs=10, batch_size=32, verbose=0)

    # Plot the Precision-Recall curve for the model based on the test set data
    precision, recall, _ = precision_recall_curve(Y_test, model.predict(X_test))
    plt.plot(recall, precision, label='Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()

    return model, plt.gca()
X = np.random.rand(100, 10)
Y = np.random.randint(0, 2, size=100)