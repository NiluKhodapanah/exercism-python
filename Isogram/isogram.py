def is_isogram(string):
    names = string.strip().lower().replace("-","").split(" ")
    for name in names:
        for c in name:
            if name.count(c) > 1:
                return False
    return True

