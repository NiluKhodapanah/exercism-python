def is_paired(input_string):
    stack = []
    brac_bras_par = {"[": "]", "{": "}", "(": ")"}

    for char in input_string:
        if char in brac_bras_par:
            stack.append(char)
        elif char in brac_bras_par.values():
            if not stack or brac_bras_par[stack[-1]] != char:
                return False
            stack.pop()
    
    return not stack
