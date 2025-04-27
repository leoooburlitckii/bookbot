from stats import get_book_text
from stats import count_of_words
from stats import number_of_each_character
from stats import sorted_list


def main():
    book_path = "/home/lepa/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_of_words(text)
    num_symbols = number_of_each_character(text)
    print(f"{num_words} words found in the document")
    print(num_symbols)
    print(sorted_list(num_symbols))







main()

