import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    # Extracting data for plotting
    months = sales_data['Month']
    product1 = sales_data['Product1']
    product2 = sales_data['Product2']
    product3 = sales_data['Product3']
    product4 = sales_data['Product4']
    product5 = sales_data['Product5']

    # Calculating standard deviations for each product
    std_dev1 = statistics.stdev(product1)
    std_dev2 = statistics.stdev(product2)
    std_dev3 = statistics.stdev(product3)
    std_dev4 = statistics.stdev(product4)
    std_dev5 = statistics.stdev(product5)

    # Creating the plot
    fig, ax = plt.subplots()
    ax.plot(months, product1, label='Product 1')
    ax.plot(months, product2, label='Product 2')
    ax.plot(months, product3, label='Product 3')
    ax.plot(months, product4, label='Product 4')
    ax.plot(months, product5, label='Product 5')

    # Adding standard deviation shading
    ax.fill_between(months, [p - std_dev for p in product1], [p + std_dev for p in product1], alpha=0.2)
    ax.fill_between(months, [p - std_dev for p in product2], [p + std_dev for p in product2], alpha=0.2)
    ax.fill_between(months, [p - std_dev for p in product3], [p + std_dev for p in product3], alpha=0.2)
    ax.fill_between(months, [p - std_dev for p in product4], [p + std_dev for p in product4], alpha=0.2)
    ax.fill_between(months, [p - std_dev for p in product5], [p + std_dev for p in product5], alpha=0.2)

    # Adding labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trends for Five Products')
    ax.legend()

    return ax