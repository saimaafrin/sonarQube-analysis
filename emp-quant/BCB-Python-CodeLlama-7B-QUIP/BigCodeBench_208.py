
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    if elements <= 0:
        raise ValueError("ValueError: elements must be a positive integer")
    np.random.seed(seed)
    steps = np.random.rand(elements) * 2 - 1
    return steps

def get_descriptive_stats(steps):
    count = len(steps)
    mean = np.mean(steps)
    std = np.std(steps)
    min = np.min(steps)
    p5 = np.percentile(steps, 5)
    p25 = np.percentile(steps, 25)
    median = np.median(steps)
    p75 = np.percentile(steps, 75)
    p95 = np.percentile(steps, 95)
    max = np.max(steps)
    return {
        "count": count,
        "mean": mean,
        "std": std,
        "min": min,
        "5th percentile": p5,
        "25th percentile": p25,
        "median": median,
        "75th percentile": p75,
        "95th percentile": p95,
        "max": max
    }

def plot_random_walk(steps):
    fig, ax = plt.subplots()
    ax.plot(steps)
    ax.set_xlabel("Steps")
    ax.set_ylabel("Value")
    ax.set_title("Random Walk")
    return fig, ax

def main():
    elements = 100
    seed = 0
    steps = task_func(elements, seed)
    descriptive_stats = get_descriptive_stats(steps)
    fig, ax = plot_random_walk(steps)
    return descriptive_stats, fig, ax