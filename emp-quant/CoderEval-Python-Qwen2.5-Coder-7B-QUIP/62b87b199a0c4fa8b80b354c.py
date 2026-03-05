def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, (list, tuple, range)):
        return seq, type(seq)
    else:
        return [seq], type(seq)