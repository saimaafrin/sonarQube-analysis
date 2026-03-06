
import pandas as pd
from sklearn.linear_model import LinearRegression

# Generate some random data
ROWS = 100
COLUMNS = ['X', 'Y']
df = pd.DataFrame(data=np.random.rand(ROWS, len(COLUMNS)), columns=COLUMNS)

# Fit the linear model
model = LinearRegression().fit(df[['X']], df['Y'])

# Print the coefficients
print(model.coef_)