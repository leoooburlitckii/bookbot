def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_of_words(text):
    words_list = text.split()
    return len(words_list)

def number_of_each_character (text):
    character_counter = {}
    for character in text:
        character_low = character.lower()
        if character_low not in character_counter:
            character_counter[character_low] = 1
        else:
            character_counter[character_low] += 1
    return character_counter

def sorted_list (dict):
    list = []
    for character in dict:
        dict_zalupka = {"name":0, "num":0}
        dict_zalupka["name"] = character
        dict_zalupka["num"] = dict[character]
        list.append(dict_zalupka)
    def key_for_sort (dict):
        return dict["num"]
    list.sort(reverse=True, key=key_for_sort)
    return list



    

