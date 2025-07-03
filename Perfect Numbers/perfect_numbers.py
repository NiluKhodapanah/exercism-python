def classify(number):
    aliqout = []
    for i in range(1, number):
        if number % i == 0:
            aliqout.append(i)
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if sum(aliqout) == number:
        return "perfect"
    elif sum(aliqout) >= number:
        return "abundant"
    else:
        return "deficient"

   