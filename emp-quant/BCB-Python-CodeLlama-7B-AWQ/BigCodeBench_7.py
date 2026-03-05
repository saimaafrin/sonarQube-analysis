import csv
import collections
import operator
def task_func(csv_file_path):
    """
    Find the best-selling product from a given CSV file with sales data.
    This function parses a CSV file assumed to have a header followed by rows containing two columns: 'product' and 'quantity'.
    It computes the total sales per product and determines the product with the highest cumulative sales.
    The CSV file must include at least these two columns, where 'product' is the name of the product as a string and 'quantity' is the number of units sold as an integer.
    Args:
        csv_file_path (str): The file path to the CSV file containing sales data.
    Returns:
        str: The name of the top-selling product based on the total quantity sold.
    """
    # Open the CSV file
    with open(csv_file_path, 'r') as csvfile:
        # Skip the header
        next(csvfile)
        # Create a dictionary to store the total sales for each product
        sales = collections.defaultdict(int)
        # Read the CSV file and update the sales dictionary
        for row in csv.reader(csvfile):
            product, quantity = row
            sales[product] += int(quantity)
        # Find the product with the highest cumulative sales
        top_seller = max(sales.items(), key=operator.itemgetter(1))[0]
    return top_seller