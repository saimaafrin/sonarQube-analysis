import csv
import collections
import operator
def task_func(csv_file_path):
    """
    Find the best-selling product from a given CSV file with sales data.
    This function parses a CSV file assumed to have a header followed by rows containing two columns: 'product' and 'quantity'. It computes the total sales per product and determines the product with the highest cumulative sales.
    The CSV file must include at least these two columns, where 'product' is the name of the product as a string and 'quantity' is the number of units sold as an integer.
    Args:
        csv_file_path (str): The file path to the CSV file containing sales data.
    Returns:
        str: The name of the top-selling product based on the total quantity sold.
    """
    # Open the CSV file
    with open(csv_file_path, 'r') as csv_file:
        # Create a dictionary to store the total sales for each product
        sales_dict = collections.defaultdict(int)
        # Read the header row
        header = next(csv.reader(csv_file))
        # Read each row of the CSV file
        for row in csv.reader(csv_file):
            # Get the product name and quantity sold
            product = row[header.index('product')]
            quantity = int(row[header.index('quantity')])
            # Add the quantity sold to the total sales for the product
            sales_dict[product] += quantity
        # Find the product with the highest cumulative sales
        top_selling_product = max(sales_dict.items(), key=operator.itemgetter(1))[0]
    return top_selling_product
csv_file_path = 'sales_data.csv'