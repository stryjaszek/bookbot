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

def sort_list(dict):
    list_of_dict = []
    for key in dict:
        list_of_dict.append({"char": key, "num": dict[key]})
    list_of_dict.sort(reverse=True, key=sort_on_nums)
    return list_of_dict

def sort_on_nums(items):
    return items["num"]