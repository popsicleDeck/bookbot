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

def sort_list(dict):
    def per(char):
        return char["num"]
    list_ = []
    for i in dict:
        if i.isalpha():
            a = {}
            a["char"]= i
            a["num"] = dict[i]
            list_.append(a)
            list_.sort(reverse=True, key=per)

    return list_
    







