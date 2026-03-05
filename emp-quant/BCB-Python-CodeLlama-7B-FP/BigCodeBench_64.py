import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Group the DataFrame by col1 and col2
    grouped_df = df.groupby(['col1', 'col2'])

    # Create a heatmap of the distribution of values in col3
    sns.heatmap(grouped_df['col3'].value_counts())

    # Return the DataFrame and the heatmap
    return df, plt.gca()
data = [
    ['a', 'b', 1],
    ['a', 'b', 2],
    ['a', 'c', 3],
    ['b', 'c', 4],
    ['b', 'c', 5],
    ['c', 'd', 6],
    ['c', 'd', 7],
    ['d', 'e', 8],
    ['d', 'e', 9],
    ['e', 'f', 10],
    ['e', 'f', 11],
    ['f', 'g', 12],
    ['f', 'g', 13],
    ['g', 'h', 14],
    ['g', 'h', 15],
    ['h', 'i', 16],
    ['h', 'i', 17],
    ['i', 'j', 18],
    ['i', 'j', 19],
    ['j', 'k', 20],
    ['j', 'k', 21],
    ['k', 'l', 22],
    ['k', 'l', 23],
    ['l', 'm', 24],
    ['l', 'm', 25],
    ['m', 'n', 26],
    ['m', 'n', 27],
    ['n', 'o', 28],
    ['n', 'o', 29],
    ['o', 'p', 30],
    ['o', 'p', 31],
    ['p', 'q', 32],
    ['p', 'q', 33],
    ['q', 'r', 34],
    ['q', 'r', 35],
    ['r', 's', 36],
    ['r', 's', 37],
    ['s', 't', 38],
    ['s', 't', 39],
    ['t', 'u', 40],
    ['t', 'u', 41],
    ['u', 'v', 42],
    ['u', 'v', 43],
    ['v', 'w', 44],
    ['v', 'w', 45],
    ['w', 'x', 46],
    ['w', 'x', 47],
    ['x', 'y', 48],
    ['x', 'y', 49],
    ['y', 'z', 50],
    ['y', 'z', 51],
    ['z', 'a', 52],
    ['z', 'a', 53],
]