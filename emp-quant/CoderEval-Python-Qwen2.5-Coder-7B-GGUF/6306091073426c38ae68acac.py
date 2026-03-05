def dict_insert(dic, val, key, *keys):
    if len(keys) == 0:
        dic[key] = val
    else:
        if key not in dic:
            dic[key] = {}
        dict_insert(dic[key], val, *keys)