
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Generate some sample data
X = np.random.rand(100, 10)
Y = np.random.randint(0, 2, 100)

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Create a Keras Sequential model with one hidden layer using a sigmoid activation function
model = keras.models.Sequential()
model.add(keras.layers.Dense(units=10, activation='sigmoid', input_shape=(10,)))
model.add(keras.layers.Dense(units=1, activation='sigmoid'))

# Compile the model with binary cross-entropy loss and an SGD optimizer
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Fit the model to the training data in a non-verbose mode
model.fit(X_train, Y_train, epochs=10, batch_size=32, verbose=0)

# Plot the ROC curve for the model on the test set
fpr, tpr, thresholds = roc_curve(Y_test, model.predict(X_test))
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend()

# Print the AUC score in the plot legend
plt.text(0.5, 0.95, 'AUC = %0.2f' % roc_auc, ha='center', va='center', fontsize=14)

# Show the plot
plt.show()

# Return the trained Keras model and the matplotlib Axes object for the ROC curve plot
return model, plt.gca()