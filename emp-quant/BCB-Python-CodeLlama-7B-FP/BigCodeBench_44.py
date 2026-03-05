from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(df):
    """
    Normalize numeric columns in a DataFrame and draw a box plot for each column.
    Missing values are replaced by column's average.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to normalize and plot.

    Returns
    -------
    DataFrame : pandas.DataFrame
        The normalized DataFrame.
    Axes : matplotlib.axes.Axes
        The box plot for each column.
    """
    # Normalize numeric columns
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Replace missing values with column average
    df_scaled = df_scaled.fillna(df_scaled.mean())

    # Draw box plot for each column
    fig, ax = plt.subplots()
    for col in df_scaled.columns:
        ax.boxplot(df_scaled[col])
    ax.set_title('Box plots for normalized columns')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')

    return df_scaled, ax
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15]})