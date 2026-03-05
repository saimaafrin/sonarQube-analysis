
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Define the model
    model = keras.models.Sequential([
        keras.layers.Dense(units=1, input_shape=(X.shape[1],), activation='sigmoid')
    ])

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='sgd')

    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=10, verbose=False)

    # Evaluate the model on the test data
    y_pred = model.predict(X_test)
    y_true = Y_test
    precision, recall, _ = precision_recall_curve(y_true, y_pred)

    # Plot the precision-recall curve
    fig, ax = plt.subplots()
    ax.plot(recall, precision)
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_title('Precision-Recall Curve')
    return model, ax