def value(colors):
    color_values = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
    code = ""
    if isinstance(colors, str) and colors in color_values:
        return color_values[colors]
#---------------------------------------------------------------------------
    if isinstance(colors, list):
        color_list = colors
        for i, color in enumerate(color_list):
            if i < 2:  
                code += str(color_values[color]) 
        return int(code) 
    else:
        color_list = colors.split("-")
        for i, color in enumerate(color_list):
            if i < 2:  
                code += str(color_values[color]) 
        return int(code) 

