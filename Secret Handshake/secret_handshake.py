def commands(binary_str):
    chain_com = []
    binary_int = int(binary_str, 2)
    bin_num = format(binary_int, "05b")
    
    if bin_num[-1] == "1":
        chain_com.append("wink")
    if bin_num[-2] == "1":
        chain_com.append("double blink")
    if bin_num[-3] == "1":
        chain_com.append("close your eyes")
    if bin_num[-4] == "1":
        chain_com.append("jump")
    if bin_num[-5] == "1":
        chain_com.reverse()

    return chain_com
