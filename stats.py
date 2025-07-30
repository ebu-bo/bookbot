def get_num_words(book_text):
    contents_split = book_text.split()
    return len(contents_split)

def get_num_count(book_text):
    character_count = {}
    lower_case = book_text.lower()
    for character in lower_case:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_in(char_count):
    def to_sort(object):
        return object["num"]

    scrambled = []
    for character, count in char_count.items():
        scrambled.append({"char": character, "num": count})

    scrambled.sort(reverse=True, key=to_sort)
    return scrambled