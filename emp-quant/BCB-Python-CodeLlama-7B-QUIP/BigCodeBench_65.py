
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50],
        'col3': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Define the columns to group by
columns_to_group_by = df.columns[:-1]

# Define the column to plot
column_to_plot = df.columns[-1]

# Group the DataFrame by the specified columns
grouped_df = df.groupby(columns_to_group_by).sum()

# Plot the DataFrame
fig, ax = plt.subplots()
ax.plot(grouped_df)

# Set the x-label and y-label
ax.set_xlabel('-'.join(columns_to_group_by))
ax.set_ylabel(column_to_plot)

# Return the DataFrame and the Axes object
return df, ax