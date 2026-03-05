import pandas as pd
from statistics import mean
def task_func(df: pd.DataFrame) -> dict:
    """
    Convert a Pandas DataFrame into a dictionary of generator objects in which each generator generates a sequence of tuples that contain a unique name and the corresponding average score for that name.
    """
    if not set(["Name", "Score"]).issubset(df.columns):
        raise ValueError("The DataFrame must have the 'Name' and 'Score' columns.")

    gen_dict = {}
    for name, score in zip(df["Name"], df["Score"]):
        if name not in gen_dict:
            gen_dict[name] = (name, mean(score))

    return gen_dict