def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    processed_sentence = sentence.lower()
    for letter in alphabet:
        if letter not in processed_sentence:
            return False        
    return True
