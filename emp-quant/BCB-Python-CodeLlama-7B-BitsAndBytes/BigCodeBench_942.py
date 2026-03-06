
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

# Generate random sales data
sales_data = pd.DataFrame(index=pd.date_range(start=START_DATE, periods=PERIODS, freq=FREQ),
                          columns=CATEGORIES,
                          data=np.random.randint(100, size=(PERIODS, len(CATEGORIES))))

# Create and visualize the sales report
fig, ax = plt.subplots()
ax.bar(sales_data.index, sales_data['Electronics'], label='Electronics')
ax.bar(sales_data.index, sales_data['Fashion'], bottom=sales_data['Electronics'], label='Fashion')
ax.bar(sales_data.index, sales_data['Home & Kitchen'], bottom=sales_data['Electronics'] + sales_data['Fashion'], label='Home & Kitchen')
ax.bar(sales_data.index, sales_data['Automotive'], bottom=sales_data['Electronics'] + sales_data['Fashion'] + sales_data['Home & Kitchen'], label='Automotive')
ax.bar(sales_data.index, sales_data['Sports'], bottom=sales_data['Electronics'] + sales_data['Fashion'] + sales_data['Home & Kitchen'] + sales_data['Automotive'], label='Sports')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.legend()
plt.show()

# Return the Matplotlib Axes object
return ax