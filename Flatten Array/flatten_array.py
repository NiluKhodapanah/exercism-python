def flatten(iterable):
    new_list = []

    for iter in iterable:

        if iter is None:
            continue
        elif not isinstance(iter, list):
            new_list.append(iter)
        else:
            new_list.extend(flatten(iter))
        
    return new_list



