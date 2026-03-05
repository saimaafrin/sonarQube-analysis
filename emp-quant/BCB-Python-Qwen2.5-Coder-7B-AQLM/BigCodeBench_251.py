
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a DataFrame")
    
    # Assuming the DataFrame has a column named 'Job' with job distribution data
    job_distribution = data['Job'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(job_distribution, labels=job_distribution.index, autopct='%1.1f%%', startangle=140)
    
    # Set the title of the pie chart
    ax.set_title('Job Distribution')
    
    return fig