def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def count_of_words(text: str) -> int:
    words_list = text.split()
    return len(words_list)

def number_of_each_character (text: str) -> dict[str,int]:
    character_counter = {}
    for character in text:
        if character.isalpha():
            character_low = character.lower()
            character_counter[character_low] = character_counter.get(character_low, 0) + 1           
    return character_counter




def from_dict_to_sorted_list (data: dict[str,int]) -> list[tuple[str,int]]:
    print(data.items())
    def key_for_sort (data1: tuple):
        return data1[1]
    sorted_list = sorted(data.items(),key=key_for_sort, reverse=True)
    return sorted_list



    

