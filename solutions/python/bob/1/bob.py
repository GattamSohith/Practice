def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"
    is_shouting = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)

    if is_shouting and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"

    if is_shouting:
        return "Whoa, chill out!"

    if hey_bob.endswith('?'):
        return "Sure."
    return "Whatever."
