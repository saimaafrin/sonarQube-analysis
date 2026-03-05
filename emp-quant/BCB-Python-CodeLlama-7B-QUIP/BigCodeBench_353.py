
import pandas as pd
import random

def task_func(product_list, categories, min_value = 10, max_value = 100):
    # Generate some random data for the products
    for product in product_list:
        product_data = {
            'Product': product,
            'Category': random.choice(categories),
            'Quantity Sold': random.randint(min_value, max_value),
            'Revenue': random.randint(min_value, max_value)
        }
        data.append(product_data)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Group the DataFrame by product and category
    grouped_df = df.groupby(['Product', 'Category']).sum()

    # Calculate the total revenue for each product
    total_revenue = grouped_df['Revenue'].sum()

    # Calculate the total quantity sold for each product
    total_quantity = grouped_df['Quantity Sold'].sum()

    # Calculate the average revenue per product
    average_revenue = total_revenue / total_quantity

    # Create a new DataFrame with the results
    results_df = pd.DataFrame({
        'Product': grouped_df.index,
        'Total Revenue': total_revenue,
        'Total Quantity': total_quantity,
        'Average Revenue': average_revenue
    })

    return results_df

results_df = task_func(product_list, categories)

print(results_df)