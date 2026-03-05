import csv
import collections
import operator
def task_func(csv_file_path):
    # Initialize a dictionary to store the total sales per product
    sales_data = collections.defaultdict(int)
    
    # Open the CSV file and read the data
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            # Add the quantity to the total sales for the product
            sales_data[product] += quantity
    
    # Find the product with the highest total sales
    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]
    
    # Return the name of the top-selling product
    return top_selling_product