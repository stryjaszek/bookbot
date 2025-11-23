def get_num_words(text):
    words = len(text.split())
    return words

def get_num_chars(text):
    chars_dict = {}
    for char in text:
        if char.lower() in chars_dict:
            chars_dict[char.lower()] += 1
        else:
            chars_dict[char.lower()] = 1
    return chars_dict