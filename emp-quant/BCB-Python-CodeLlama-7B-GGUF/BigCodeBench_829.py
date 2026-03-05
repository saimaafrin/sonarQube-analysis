
import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    """
    Convert a Pandas DataFrame into a dictionary of generator objects in which each generator generates a sequence of tuples that contain a unique name and the corresponding average score for that name.

    :param df: A Pandas DataFrame with columns 'Name' and 'Score'
    :return: A dictionary of generator objects
    """
    if not set(["Name", "Score"]).issubset(df.columns):
        raise ValueError("The DataFrame must have columns 'Name' and 'Score'")

    name_score_pairs = df.groupby("Name")["Score"].mean().to_dict()
    gen_dict = {name: (name, score) for name, score in name_score_pairs.items()}
    return gen_dict

df_sample = pd.DataFrame({
    "Name": ["Micky", "Donald", "Girl"],
    "Score": [25.2, 9, -1]
})

gen_dict = task_func(df_sample)
print({key: next(value) for key, value in gen_dict.items()})