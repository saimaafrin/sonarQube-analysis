def _shuffled(seq: Sequence[str]) -> list[str]:
	"""
	Shuffle a given seq with the given FIXED_RANDOM_SEED
	"""
	return random.Random(FIXED_RANDOM_SEED).sample(seq, len(seq))