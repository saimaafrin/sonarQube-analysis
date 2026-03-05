
import csv
import collections
import operator

def task_func(csv_file_path):
    # Initialize a dictionary to store the total sales per product
    product_sales = collections.defaultdict(int)

    # Open the CSV file and read the data
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            product_sales[product] += quantity

    # Find the product with the highest total sales
    top_selling_product = max(product_sales.items(), key=operator.itemgetter(1))

    # Return the name of the top-selling product
    return top_selling_product[0]