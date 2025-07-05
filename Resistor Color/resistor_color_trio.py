def label(colors):
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
    zeros = 0
    for i, color in enumerate(colors[:3]):
        if i < 2:
            code += str(color_values[color])
        else:
            zeros = color_values[color]
    
    final_value = int(code) * (10 ** zeros)

    if final_value == 0: 
        return "0 ohms"
    elif final_value % 1_000_000_000 == 0:
        return f"{final_value // 1_000_000_000} gigaohms"
    elif final_value % 1_000_000 == 0:
        return f"{final_value // 1_000_000} megaohms"
    elif final_value % 1_000 == 0:
        return f"{final_value // 1_000} kiloohms"
    else:
        return f"{final_value} ohms"
