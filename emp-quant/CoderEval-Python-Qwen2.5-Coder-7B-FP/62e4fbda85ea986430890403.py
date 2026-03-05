def _shuffled(seq: Sequence[str]) -> list[str]:
# Create a copy of the sequence to avoid modifying the original
	shuffled_seq = list(seq)
	
	# Shuffle the copied sequence using the fixed random seed
	random.seed(FIXED_RANDOM_SEED)
	random.shuffle(shuffled_seq)
	
	return shuffled_seq