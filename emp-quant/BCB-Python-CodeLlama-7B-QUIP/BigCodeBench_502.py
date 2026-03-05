
from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns

def task_func(days_in_past=7, random_seed=0):
    random.seed(random_seed)
    df = pd.DataFrame(index=range(days_in_past))
    df['Date'] = pd.date_range(start=datetime.today() - timedelta(days=days_in_past), periods=days_in_past)
    df['Activity'] = random.choices(['Running', 'Swimming', 'Cycling', 'Yoga', 'Weight Training'], k=days_in_past)
    df['Duration'] = random.randint(0, 120, size=days_in_past)
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['Activity'] = df['Activity'].map({'Running': 'Running', 'Swimming': 'Swimming', 'Cycling': 'Cycling', 'Yoga': 'Yoga', 'Weight Training': 'Weight Training'})
    df = df.set_index('Date').unstack().reset_index().set_index('Activity').unstack().reset_index()
    ax = sns.lineplot(x='Date', y='Duration', hue='Activity', data=df)
    return ax, df