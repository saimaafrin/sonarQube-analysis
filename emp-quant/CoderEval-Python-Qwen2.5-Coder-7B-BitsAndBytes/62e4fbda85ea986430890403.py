import random

FIXED_RANDOM_SEED = 42

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Shuffle a given seq with the given FIXED_RANDOM_SEED
    """
    shuffled_seq = list(seq)
    random.seed(FIXED_RANDOM_SEED)
    random.shuffle(shuffled_seq)
    return shuffled_seq