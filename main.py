from stats import get_char_count_dict, get_num_words

book_name = "frankenstein"
path = f"books/{book_name}.txt"


def get_book_text(path):
    with open(path) as file:
        book = file.read()
    return book


def main():
    book = get_book_text(path)
    num_words = get_num_words(book)
    # print(book)
    print(f"{num_words} words found in the document")
    print(get_char_count_dict(book))


main()
