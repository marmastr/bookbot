def get_book_text(path):
    with open(path) as file:
        book = file.read()
    return book


def get_word_count(book_text):
    count = len(book_text.split())
    return count


def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book)
    # print(book)
    print(f"{num_words} words found in the document")


main()
