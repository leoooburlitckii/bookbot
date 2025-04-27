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

