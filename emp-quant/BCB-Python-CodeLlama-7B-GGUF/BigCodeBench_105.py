
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df):
    # Check if dataframe is empty
    if df.empty:
        raise ValueError("Dataframe is empty")

    # Check if required columns are missing
    required_columns = ["date", "value1", "value2"]
    if not all(column in df.columns for column in required_columns):
        raise ValueError("Required columns are missing")

    # Check if 'date' column is in datetime format
    if not pd.to_datetime(df["date"]).is_datetime64:
        raise ValueError("'date' column is not in datetime format")

    # Convert 'date' column to ordinal format
    df["date"] = pd.to_datetime(df["date"]).dt.to_period("D")

    # Create correlation matrix
    corr_matrix = df.corr()

    # Generate correlation matrix heatmap
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")

    # Generate pair plot
    sns.pairplot(df, diag_kind="kde")

    return fig, ax