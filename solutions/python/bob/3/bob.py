"""Bob response module."""

def response(hey_bob):
    """Return Bob's response based on the input."""
    phrase = hey_bob.strip()

    if not phrase:
        return "Fine. Be that way!"

    if phrase.isupper() and phrase.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if phrase.endswith("?"):
        return "Sure."

    if phrase.isupper():
        return "Whoa, chill out!"

    return "Whatever."
