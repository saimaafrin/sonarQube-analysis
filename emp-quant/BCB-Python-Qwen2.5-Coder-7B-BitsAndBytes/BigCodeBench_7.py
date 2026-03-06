
import csv
import collections

def task_func(csv_file_path):
    # Initialize a dictionary to store the total sales for each product
    sales_data = collections.defaultdict(int)
    
    # Open the CSV file and read the data
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            
            # Add the quantity to the total sales for this product
            sales_data[product] += quantity
    
    # Find the product with the maximum total sales
    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]
    
    return top_selling_product