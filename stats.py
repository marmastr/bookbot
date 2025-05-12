def get_num_words(book_text):
    count = len(book_text.split())
    return count


def get_char_count_dict(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    # char_dict_sorted = dict(sorted(char_dict.items()))
    return char_dict


def sort_on(dict):
    return dict["num"]


def get_char_dict_sorted(book_text):
    char_dict = get_char_count_dict(book_text)
    char_list_dict = []
    for key in char_dict:
        char_list_dict.append({"name": key, "num": char_dict[key]})
    char_list_dict.sort(reverse=True, key=sort_on)
    return char_list_dict
