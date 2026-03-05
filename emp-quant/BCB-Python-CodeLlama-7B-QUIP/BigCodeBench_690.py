
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a random dataset
data = pd.DataFrame(np.random.rand(ROWS, COLUMNS))

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(data)

# Print the coefficients
print(model.coef_)