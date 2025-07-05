def resistor_label(colors):
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

    tol_values = {
    "silver": 10,
    "gold": 5,
    "red": 2,
    "brown": 1,
    "green": 0.5,
    "blue": 0.25,
    "violet": 0.1,
    "grey": 0.05,
}
    code = ""
    zeros = 0

    if len(colors) == 1:
        return "0 ohms"
    
    elif len(colors) == 4:
        for i, color in enumerate(colors[:2]):
            code += str(color_values[color])
            zeros = color_values[colors[2]]

        final_value = int(code) * (10 ** zeros)

        if final_value == 0: 
                return "0 ohms"
        elif final_value >= 1_000_000_000 :
                return f"{final_value / 1_000_000_000:g} gigaohms ±{tol_values[colors[3]]}%"
        elif final_value >= 1_000_000 :
                return f"{final_value / 1_000_000:g} megaohms ±{tol_values[colors[3]]}%"
        elif final_value >= 1_000 :
                return f"{final_value / 1_000:g} kiloohms ±{tol_values[colors[3]]}%"
        else:
                return f"{final_value} ohms ±{tol_values[colors[3]]}%"

    else:
        for i, color in enumerate(colors[:3]):
            code += str(color_values[color])
            zeros = color_values[colors[3]]
        final_value = int(code) * (10 ** zeros)

        if final_value == 0: 
            return "0 ohms"
        elif final_value >= 1_000_000_000 :
            return f"{final_value / 1_000_000_000:g} gigaohms ±{tol_values[colors[4]]}%"
        elif final_value >= 1_000_000 :
            return f"{final_value / 1_000_000:g} megaohms ±{tol_values[colors[4]]}%"
        elif final_value >= 1_000 :
            return f"{final_value / 1_000:g} kiloohms ±{tol_values[colors[4]]}%"
        else:
            return f"{final_value} ohms ±{tol_values[colors[4]]}%"
        
