import sys
from stats import get_book_text
from stats import count_of_words
from stats import number_of_each_character
from stats import from_dict_to_sorted_list 


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_of_words(text)
    num_symbols = number_of_each_character(text)
    list_with_characters = from_dict_to_sorted_list(num_symbols)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in list_with_characters:
        a,b = i[0], i[1]
        print(f"{a}: {b}")
    print("============= END ===============")
    
    







main()

