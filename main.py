from stats import get_num_words, get_char_dict_sorted

book_name = "frankenstein"
book_path = f"books/{book_name}.txt"


def get_book_text(path):
    with open(path) as file:
        book = file.read()
    return book


def pretty_print(book, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    sorted_letter_list = get_char_dict_sorted(book)
    for dict in sorted_letter_list:
        if dict["name"].isalpha():
            print(f"{dict['name']}: {dict['num']}")
    print("============= END ===============")


def main():
    book_txt = get_book_text(book_path)
    pretty_print(book_txt, book_path)


#    print(get_char_count_dict(book))


main()
