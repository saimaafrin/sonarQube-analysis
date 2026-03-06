
import pandas as pd
import matplotlib.pyplot as plt

# Create a list of dictionaries with the same keys (fruit names)
data = [
    {'fruit': 'apple', 'time': 1, 'sales': 10},
    {'fruit': 'apple', 'time': 2, 'sales': 20},
    {'fruit': 'banana', 'time': 1, 'sales': 30},
    {'fruit': 'banana', 'time': 2, 'sales': 40},
    {'fruit': 'orange', 'time': 1, 'sales': 50},
    {'fruit': 'orange', 'time': 2, 'sales': 60}
]

# Combine the list of dictionaries into a single pandas dataframe
df = pd.DataFrame(data)

# Fill NA/NaN values with 0
df = df.fillna(0)

# Generate a line chart of sales
ax = df.plot(kind='line', x='time', y='sales', title='Fruit Sales over Time')

# Set the x-axis and y-axis labels
ax.set_xlabel('Time')
ax.set_ylabel('Sales Quantity')

# Show the plot
plt.show()