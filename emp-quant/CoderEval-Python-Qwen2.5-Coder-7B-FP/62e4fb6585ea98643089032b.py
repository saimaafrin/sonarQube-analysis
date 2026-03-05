def parse_version(s: str) -> tuple[int, ...]:
# Split the input string by dots and convert each part to an integer
	return tuple(int(part) for part in s.split('.'))