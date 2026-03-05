def is_fill_request_seq(seq):
    return isinstance(seq, list) and all(isinstance(item, dict) for item in seq)