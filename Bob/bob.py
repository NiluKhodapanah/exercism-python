def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return("Sure.")
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif len(hey_bob) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."

