
import string
import matplotlib.pyplot as plt

def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    # Create a bar subplot
    fig, ax = plt.subplots()
    ax.bar(freq.keys(), freq.values())
    ax.set_xlabel("Letters")
    ax.set_ylabel("Frequency")
    ax.set_title("Letter Frequencies")

    return freq, fig