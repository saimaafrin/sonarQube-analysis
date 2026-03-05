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
    # Open the CSV file and read its contents
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)
        # Create a dictionary to store the total sales for each product
        product_totals = collections.defaultdict(int)
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            # Extract the product name and quantity sold
            product_name = row[0]
            quantity_sold = int(row[1])
            # Add the quantity sold to the total sales for the product
            product_totals[product_name] += quantity_sold
        # Find the product with the highest cumulative sales
        top_selling_product = max(product_totals, key=operator.itemgetter(1))
        # Return the name of the top-selling product
        return top_selling_product
csv_file_path = 'sales_data.csv'