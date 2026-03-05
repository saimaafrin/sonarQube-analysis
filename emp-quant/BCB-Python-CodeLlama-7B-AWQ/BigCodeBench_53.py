import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
COLUMN_NAMES = ["Name", "Email", "Age", "Country"]
def task_func(text):
    """
    Extract data from a text and create a Pandas DataFrame.
    The text contains several lines, each formatted as 'Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA'.
    Plot the age distribution using seaborn.
    The data is extracted using the regular expression pattern: "Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)" and the resulting DataFrame has columns: ['Name', 'Email', 'Age', 'Country']
    """
    # Extract data from text using regular expression
    data = re.findall(r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)", text)

    # Create a Pandas DataFrame from extracted data
    df = pd.DataFrame(data, columns=COLUMN_NAMES)

    # Plot age distribution using seaborn
    sns.countplot(x="Age", data=df)
    plt.show()

    return df
text = """
Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA
Name: Jane Doe, Email: jane.doe@example.com, Age: 25, Country: USA
Name: Bob Smith, Email: bob.smith@example.com, Age: 40, Country: Canada
"""