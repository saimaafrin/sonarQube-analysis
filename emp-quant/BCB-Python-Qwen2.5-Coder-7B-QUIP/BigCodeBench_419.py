
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Construct a Keras Sequential model
    model = keras.Sequential([
        keras.layers.Dense(10, input_shape=(X.shape[1],), activation='sigmoid')
    ])

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

    # Fit the model to the training data
    model.fit(X_train, Y_train, verbose=0, epochs=10)

    # Get the predictions for the test set
    Y_pred = model.predict(X_test)

    # Calculate precision and recall
    precision, recall, _ = precision_recall_curve(Y_test, Y_pred)

    # Plot the Precision-Recall curve
    plt.figure()
    plt.plot(recall, precision, marker='.')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')

    # Return the model and the axes object
    return model, plt.gca()