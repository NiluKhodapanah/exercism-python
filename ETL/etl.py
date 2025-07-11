def transform(legacy_data):
    new_dict = {}
    for k, v in legacy_data.items():
        for letter in v:
            letter = letter.lower()
            new_dict.update({letter: k})
    return new_dict
        
            
