from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt
def task_func(X, Y):
    # Split data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Construct and compile the model
    model = keras.Sequential()
    model.add(keras.layers.Dense(64, activation='sigmoid', input_shape=(X.shape[1],)))
    model.compile(loss='binary_crossentropy', optimizer='sgd')

    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=10, verbose=0)

    # Evaluate the model on the test data
    Y_pred = model.predict(X_test)
    Y_pred_class = Y_pred > 0.5
    precision, recall, _ = precision_recall_curve(Y_test, Y_pred_class)

    # Plot the Precision-Recall curve
    plt.plot(recall, precision, label='Precision-Recall curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()

    return model, plt.gca()
X = np.random.rand(100, 10)
Y = np.random.randint(0, 2, 100)