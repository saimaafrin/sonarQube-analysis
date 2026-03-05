def is_none_string(val: any) -> bool:
# Check if the input value is a string and if it is equal to 'none' (case-insensitive)
	return isinstance(val, str) and val.lower() == 'none'