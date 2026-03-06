
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Construct the Keras Sequential model
    model = keras.Sequential()
    model.add(keras.layers.Dense(units=64, activation='sigmoid', input_shape=(X.shape[1],)))
    model.add(keras.layers.Dense(units=1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=10, batch_size=32, verbose=0)

    # Plot the Precision-Recall curve for the test set
    precision, recall, thresholds = precision_recall_curve(Y_test, model.predict(X_test))
    plt.plot(recall, precision, label='Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()

    return model, plt.gca()