
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Create a Sequential model with a single hidden layer
    model = keras.models.Sequential([
        keras.layers.Dense(1, input_shape[1], activation='sigmoid')
    ])

    # Compile the model with binary cross-entropy loss and an SGD optimizer
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])

    # Fit the model to the training data in a non-verbose mode
    model.fit(X_train, Y_train, epochs=100, verbose=False)

    # Evaluate the model on the test set
    Y_pred = model.predict(X_test)
    Y_pred_class = np.where(Y_pred > 0.5, 1, 0)
    test_labels = np.where(Y_test > 0.5, 1, 0)
    test_auc = auc(test_labels, Y_pred_class)
    roc_curve_data = roc_curve(test_labels, Y_pred_class)

    # Plot the ROC curve
    plt.figure(figsize=(8, 8))
    plt.plot(roc_curve_data[:, 0], roc_curve_data[:, 1], label='ROC curve')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend()
    plt.show()

    return model, roc_curve_data