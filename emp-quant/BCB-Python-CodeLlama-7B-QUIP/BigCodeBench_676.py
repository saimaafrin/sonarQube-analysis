
import pandas as pd
import random

def task_func(df):
    df['winner'] = df.apply(lambda x: x.max(), axis=1)
    if df['winner'] == df['winner'].max():
        df['winner'] = random.choice(df['winner'])
    return df