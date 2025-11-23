from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_num_words = get_num_words(book_text)
    print(f"Found {book_num_words} total words")

def get_book_text(path):
    with open(path) as book:
        text = book.read()
        return text

main()