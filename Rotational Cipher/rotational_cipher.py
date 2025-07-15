def rotate(text, key):
    key = int(key) % 26
    alph = "abcdefghijklmnopqrstuvwxyz"
    
    sentence = ""
    
    for t in text:
        if t.lower() in alph: 
            t_no = alph.index(t.lower())
            new_letter = alph[(t_no+key)%26]

            if t.isupper():
                sentence += new_letter.upper()
            else:
                sentence += new_letter
            
        else:
            sentence += t    
    return sentence

            
        