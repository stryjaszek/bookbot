from stats import get_num_words
from stats import get_num_chars
from stats import sort_list

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_num_words = get_num_words(book_text)
    book_num_chars = get_num_chars(book_text)
    sorted_list = sort_list(book_num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {book_num_words} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        if element["char"].isalpha() == True:
            print(f'{element["char"]}: {element["num"]}')
    print("============= END ===============")

def get_book_text(path):
    with open(path) as book:
        text = book.read()
        return text

main()