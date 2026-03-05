
import csv
import collections
import operator

def task_func(csv_file_path):
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        product_sales = collections.defaultdict(int)
        for row in reader:
            product_sales[row["product"]] += int(row["quantity"])
        top_product = max(product_sales, key=operator.itemgetter(1))
        return top_product