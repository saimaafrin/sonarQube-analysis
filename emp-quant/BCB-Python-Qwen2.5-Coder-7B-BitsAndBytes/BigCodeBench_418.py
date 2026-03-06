
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def task_func(X, Y):
    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    # Create a Keras Sequential model
    model = keras.Sequential([
        keras.layers.Dense(1, input_shape=(X_train.shape[1],), activation='sigmoid')
    ])
    
    # Compile the model
    model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.01),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    # Fit the model to the training data
    model.fit(X_train, Y_train, epochs=50, verbose=0)
    
    # Predict probabilities on the test set
    Y_pred_prob = model.predict(X_test)
    
    # Compute ROC curve and AUC
    fpr, tpr, thresholds = roc_curve(Y_test, Y_pred_prob)
    roc_auc = auc(fpr, tpr)
    
    # Plot the ROC curve
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()
    
    return model, plt.gca()