import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
def task_func(X, Y):
    # Split data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Create and compile model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='sigmoid', input_shape=(X.shape[1],)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

    # Train model
    model.fit(X_train, Y_train, epochs=10, batch_size=32, verbose=0)

    # Evaluate model on test set
    Y_pred = model.predict(X_test)
    Y_pred_class = np.where(Y_pred > 0.5, 1, 0)
    Y_test_class = np.where(Y_test > 0.5, 1, 0)
    fpr, tpr, _ = roc_curve(Y_test_class, Y_pred_class)
    roc_auc = auc(fpr, tpr)

    # Plot ROC curve
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend()
    plt.show()

    return model, plt.gca()
X = np.random.rand(1000, 10)
Y = np.random.rand(1000) > 0.5