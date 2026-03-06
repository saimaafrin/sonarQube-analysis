
import csv
import collections
import operator

def task_func(csv_file_path):
    # Open the CSV file and read it into a dictionary
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        sales_data = {row['product']: int(row['quantity']) for row in reader}

    # Compute the total sales per product
    total_sales = collections.Counter(sales_data)

    # Determine the product with the highest cumulative sales
    top_selling_product = max(total_sales, key=operator.itemgetter(1))

    # Return the name of the top-selling product
    return top_selling_product