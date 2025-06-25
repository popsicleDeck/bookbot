def words_counter(text):
    return len(text)

def char_counter(text):
    text = text.lower()
    dict_ = {}
    for char in text:
        if char not in dict_:
            dict_[char] = 0
        dict_[char] += 1
    return dict_

