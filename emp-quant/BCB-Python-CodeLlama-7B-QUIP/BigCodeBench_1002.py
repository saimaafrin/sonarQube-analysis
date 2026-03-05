
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column_name="target_column"):
    # Convert the JSON data to a Pandas DataFrame
    df = pd.json.loads(data)

    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame")

    # Convert non-numeric columns to categorical type and then to numeric codes
    df = df.apply(lambda x: x if x.dtype.kind == "f" else x.astype("category").cat.codes)

    # Plot a histogram of the specified column
    fig, ax = plt.subplots()
    ax.hist(df[column_name], bins=50, label=column_name)
    ax.set_xlabel(column_name)
    ax.set_title(f"Histogram of {column_name}")
    plt.show()

    return df, ax