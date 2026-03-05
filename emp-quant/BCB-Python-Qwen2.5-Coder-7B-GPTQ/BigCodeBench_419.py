from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt
def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    # Determine the input dimension based on the first feature set of X
    input_dim = X_train.shape[1]
    
    # Construct a Keras Sequential model
    model = keras.Sequential([
        keras.layers.Dense(1, input_dim=input_dim, activation='sigmoid')
    ])
    
    # Compile the model
    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=10, verbose=0)
    
    # Get the predicted probabilities for the test set
    Y_pred = model.predict(X_test)
    
    # Calculate precision and recall
    precision, recall, _ = precision_recall_curve(Y_test, Y_pred)
    
    # Plot the Precision-Recall curve
    plt.figure()
    plt.plot(recall, precision, marker='.')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.show()
    
    # Return the trained model and the axes object for the plot
    return model, plt.gca()