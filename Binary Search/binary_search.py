def binary_search(search_list, item):
    start_index = 0 
    
    while len(search_list) > 0:
        mid_index = len(search_list) // 2
        mid_value = search_list[mid_index]
        
        if mid_value == item:
            return start_index + mid_index
        elif mid_value > item:
            search_list = search_list[:mid_index]
        else:
            start_index = start_index + mid_index + 1
            search_list = search_list[mid_index + 1:]
            
    raise ValueError("value not in array")