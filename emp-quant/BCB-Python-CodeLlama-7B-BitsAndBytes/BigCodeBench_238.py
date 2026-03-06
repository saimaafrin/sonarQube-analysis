
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize the 'Age' and 'Score' columns
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df[['Age', 'Score']])

    # Remove duplicates based on 'Name'
    df_std = df_std.drop_duplicates(subset='Name', keep='first')

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df_std['Age (standardized)'], df_std['Score (standardized)'], c='blue')
    ax.set_title('Scatter Plot of Standardized Age and Score')
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    plt.show()

    return df_std, ax