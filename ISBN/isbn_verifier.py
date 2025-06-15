def is_valid(isbn):
    isbn = list(isbn.replace("-",""))
    isbn_sum = 0

    if len(isbn) != 10:
        return False
    
    for i, char in enumerate(isbn):
        if i < 9:
            if char.isdigit():
                isbn_sum += (10-i) * int(char)
            else:
                return False
            
        else:
            if char.isdigit():
                isbn_sum += (10-i) * int(char)
            elif char.upper() == "X":
                isbn_sum += 10
            else:
                return False
            
    return isbn_sum % 11 == 0