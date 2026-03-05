
import pandas as pd
from sklearn.linear_model import LinearRegression

# Generate random data
np.random.seed(0)
data = pd.DataFrame(np.random.rand(ROWS, COLUMNS), columns=COLUMNS)

# Fit linear regression model
model = LinearRegression().fit(data[['X']], data['Y'])

# Print model summary
print(model.summary())