
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Generate random sales figures for each product over 12 months
PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]
sales_data = pd.DataFrame(np.random.randint(100, size=(12, 5)), columns=PRODUCTS, index=MONTHS)

# Plot the total sales per product using a line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=sales_data, x=MONTHS, y=PRODUCTS)
plt.title('Total Sales per Product')
plt.xlabel('Month')
plt.ylabel('Product')
plt.show()

# Plot the sales figures across products and months using a heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(sales_data, annot=True, cmap='coolwarm')
plt.title('Sales Figures Across Products and Months')
plt.xlabel('Product')
plt.ylabel('Month')
plt.show()