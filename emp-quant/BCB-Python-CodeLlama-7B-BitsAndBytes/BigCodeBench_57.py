
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Calculate the correlation matrix of the DataFrame
    corr = df.corr()

    # Round each correlation to 2 decimals
    corr = corr.round(2)

    # Create a heatmap of the correlation matrix
    sns.heatmap(corr, annot=True, cmap="coolwarm")

    # Set the title of the plot
    plt.title(title)

    # Show the plot
    plt.show()

# Call the function with the desired arguments
task_func("data.csv", "Correlation Matrix")