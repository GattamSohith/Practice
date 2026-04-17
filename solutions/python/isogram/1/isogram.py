def is_isogram(string):
    seen_letters = []
    for s in string.lower():
        if s.isalpha():
            if s in seen_letters:
                return False
            seen_letters.append(s)
    return True