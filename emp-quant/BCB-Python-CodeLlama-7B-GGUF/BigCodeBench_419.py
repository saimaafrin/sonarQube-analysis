
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    # Construct Keras Sequential model
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(64, activation='sigmoid', input_shape=(X.shape[1],)))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
    
    # Fit model to training data
    model.fit(X_train, Y_train, epochs=10, batch_size=32, verbose=0)
    
    # Evaluate model on test data
    Y_pred = model.predict(X_test)
    Y_pred_class = (Y_pred > 0.5).astype(int)
    test_acc = model.evaluate(X_test, Y_test, verbose=0)
    print(f'Test accuracy: {test_acc:.3f}')
    
    # Plot Precision-Recall curve
    precision, recall, _ = precision_recall_curve(Y_test, Y_pred_class)
    plt.plot(recall, precision, label='Precision-Recall curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.show()
    
    return model, plt.gca()