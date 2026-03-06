
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df):
    # Split the DataFrame into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.3, random_state=42)
    return (X_train, X_test, y_train, y_test)

# Load the DataFrame from a CSV file
df = pd.read_csv('data.csv')

# Call the function and print the results
result = task_func(df)
print(result)