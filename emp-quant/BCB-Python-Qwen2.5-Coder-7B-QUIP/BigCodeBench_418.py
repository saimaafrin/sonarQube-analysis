
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Create a Sequential model with one hidden layer
    model = keras.Sequential([
        keras.layers.Dense(10, input_shape=(X_train.shape[1],), activation='sigmoid')
    ])

    # Compile the model with binary cross-entropy loss and an SGD optimizer
    model.compile(loss='binary_crossentropy', optimizer=keras.optimizers.SGD(learning_rate=0.01), metrics=['accuracy'])

    # Fit the model to the training data
    model.fit(X_train, Y_train, verbose=0, epochs=10)

    # Calculate the ROC curve and AUC score
    Y_pred = model.predict(X_test)
    fpr, tpr, _ = roc_curve(Y_test, Y_pred)
    roc_auc = auc(fpr, tpr)

    # Plot the ROC curve
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc="lower right")

    # Return the trained model and the Axes object
    return model, plt