def is_fill_request_seq(seq):
    """
    Check whether seq can be converted to FillRequestSeq and bool is returned.
    """
    return isinstance(seq, list) and all(isinstance(item, dict) for item in seq)