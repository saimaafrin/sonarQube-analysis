
import itertools
from typing import Any
from scipy import stats

def task_func(input_list: list, repetitions: int) -> Any:
    flattened_list = list(itertools.chain.from_iterable([input_list] * repetitions))
    mode_result = stats.mode(flattened_list)
    return mode_result