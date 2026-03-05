def round_half_to_even(n):
# Check if the fractional part is exactly 0.5
	if n % 1 == 0.5:
		# Round half to even (bankers' rounding)
		return int(n + 0.5) if n > 0 else int(n - 0.5)
	else:
		# Use standard rounding for other cases
		return round(n)