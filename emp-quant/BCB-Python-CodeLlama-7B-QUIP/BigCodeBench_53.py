
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    pattern = "Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)"
    matches = re.findall(pattern, text, re.MULTILINE)
    data = []
    for match in matches:
        data.append(match)
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    return df

def plot_age_distribution(df):
    sns.countplot(x="Age", data=df)
    plt.show()

def main():
    text = "Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA\nName: Jane Doe, Email: jane.doe@example.com, Age: 25, Country: USA\nName: Bob Smith, Email: bob.smith@example.com, Age: 40, Country: USA"
    df = task_func(text)
    plot_age_distribution(df)