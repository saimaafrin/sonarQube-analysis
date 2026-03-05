
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    # Create a Keras Sequential model with one hidden layer
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(64, activation='sigmoid', input_shape=(X.shape[1],)))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    
    # Compile the model with binary cross-entropy loss and SGD optimizer
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
    
    # Fit the model to the training data in a non-verbose mode
    model.fit(X_train, Y_train, epochs=100, batch_size=32, verbose=0)
    
    # Plot the ROC curve for the model on the test set
    fpr, tpr, thresholds = roc_curve(Y_test, model.predict(X_test))
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc='lower right')
    plt.show()
    
    return model, plt.gca()