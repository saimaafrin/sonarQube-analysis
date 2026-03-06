
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create a sample DataFrame with random numeric values
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to the DataFrame
scaler.fit(df)

# Transform the DataFrame using the scaler
df_standardized = scaler.transform(df)

# Print the standardized DataFrame
print(df_standardized)