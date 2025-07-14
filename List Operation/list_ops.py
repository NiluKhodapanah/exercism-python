def append(lst1, lst2):
    result = []
    for item in lst1:
        result.append(item)
    for item in lst2:
        result.append(item)
    return result


def concat(lists):
    result = []
    for list in lists:
        for e in list:
            result.append(e)
    return result
        


def filter(function, list):
    result = []
    for l in list:
        if function(l) == True:
            result.append(l)
    return result
            


def length(list):
    result = 0
    for e in list:
        result += 1
    return result
        


def map(function, list):
    result = []
    for l in list:
        result.append(function(l))
    return result


def foldl(function, list, initial):
    init = initial
    for l in list:
        init = function(init, l)
    return init
        


def foldr(function, list, initial):
    list = list[::-1]
    init = initial
    for l in list:
        init = function(init, l)
    return init
        

def reverse(list):
    return list[::-1]