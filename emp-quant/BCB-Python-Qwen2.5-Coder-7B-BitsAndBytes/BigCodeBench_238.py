
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize the 'Age' and 'Score' columns
    scaler = StandardScaler()
    df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])
    
    # Remove duplicate entries based on 'Name'
    df = df.drop_duplicates(subset='Name')
    
    # Create a scatter plot of the standardized values
    fig, ax = plt.subplots()
    ax.scatter(df['Age'], df['Score'])
    ax.set_title('Scatter Plot of Standardized Age and Score')
    ax.set_xlabel('Age (standardized)')
    ax.set_ylabel('Score (standardized)')
    
    return df, ax