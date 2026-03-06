
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    # Extract data from text using regular expression
    data = re.findall(r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)", text)

    # Create a Pandas DataFrame from the extracted data
    df = pd.DataFrame(data, columns=COLUMN_NAMES)

    # Plot the age distribution using seaborn
    sns.countplot(x="Age", data=df)
    plt.show()

    return df

df = task_func(text)
print(df)