
import pandas as pd
import seaborn as sns

def task_func(data=None):
    if data is None:
        data = pd.read_csv("data.csv")
    weight_string = data["Weight_String"]
    height = data["Height"]
    weight = [float(w) for w in weight_string]
    height = [float(h) for h in height]
    fig, ax = plt.subplots()
    ax.scatter(weight, height)
    ax.set_xlabel("Weight")
    ax.set_ylabel("Height")
    ax.set_title("Weight vs Height")
    return ax