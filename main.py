from stats import get_book_text
from stats import count_of_words
from stats import number_of_each_character
from stats import sorted_list


def main():
    book_path = "/home/lepa/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_of_words(text)
    num_symbols = number_of_each_character(text)
    list_with_characters = sorted_list(num_symbols)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(list_with_characters)):
        a = list_with_characters[i]["name"]
        b = list_with_characters[i]["num"]
        if a.isalpha():
            print(f"{a}: {b}")
    print("============= END ===============")

    







main()

