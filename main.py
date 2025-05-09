def get_book_text(path):
    with open(path) as file:
        book = file.read()
    return book


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
