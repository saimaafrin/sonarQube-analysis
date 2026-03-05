
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a DataFrame")
    
    # Assuming the DataFrame has a column named 'Job' with job distribution data
    job_distribution = data['Job'].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(job_distribution, labels=job_distribution.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return fig