
import pandas as pd
import matplotlib.pyplot as plt

# Define the columns of the DataFrame
COLUMNS = ['col1', 'col2', 'col3']

# Create a sample DataFrame
data = {'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50],
        'col3': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data, columns=COLUMNS)

# Group the DataFrame by the first two columns
grouped_df = df.groupby(df.columns[:-1])

# Create a line chart with unique values in the last column
ax = grouped_df.plot(kind='line', x=df.columns[:-1], y=df.columns[-1])

# Set the x-label and y-label
ax.set_xlabel('-'.join(df.columns[:-1]))
ax.set_ylabel(df.columns[-1])

# Return the DataFrame and Axes object
return df, ax