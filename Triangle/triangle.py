# implement a func with three parameters
def equilateral(lst):
    a = lst[0]
    b = lst[1]
    c = lst[2]
# check the conditions
    for l in lst:
        if l <= 0 :
            return False
    if a + b <= c or a + c <= b or c + b <= a:
        return False
    if a == b == c :
        return True
    else:
        return False
    
# implement a func with three parameters

#--------------------------
def isosceles(lst):
    a = lst[0]
    b = lst[1]
    c = lst[2]
# check the conditions
    for l in lst:
        if l <= 0 :
            return False
    if a + b <= c or a + c <= b or c + b <= a:
        return False
    if a == b or a == c or b == c :
        return True
    else:
        return False
#---------------------------

# implement a func with three parameters
def scalene(lst):
    a = lst[0]
    b = lst[1]
    c = lst[2]
# check the conditions
    for l in lst:
        if l <= 0 :
            return False
    if a + b <= c or a + c <= b or c + b <= a:
        return False
    if a != b and a!= c and b!=c :
        return True
    else:
        return False
    