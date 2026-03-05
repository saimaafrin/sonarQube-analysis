import random
from typing import Sequence

FIXED_RANDOM_SEED = 42

def _shuffled(seq: Sequence[str]) -> list[str]:
    random.seed(FIXED_RANDOM_SEED)
    return list(random.sample(seq, len(seq)))