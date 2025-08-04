
def get_num_words(phrase):
    number_of_words = 0
    phrase = phrase.split()
    number_of_words = len(phrase)
    return number_of_words

def sort_on(items):
    return items["num"]

def get_dict_letters(phrase):
    dict_letters = {}
    for letter in phrase:
        letter = letter.lower()
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1

    list_of_letters = []
    for key, value in dict_letters.items():
        list_of_letters.append({"char": key, "num": value})

    list_of_letters.sort(reverse=True, key=sort_on)

    return list_of_letters

