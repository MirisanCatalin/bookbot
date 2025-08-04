import sys

from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    f.close()

    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    try:
        book_text = get_book_text(path_to_file)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
        
    number_of_words = get_num_words(book_text)

    print(f"Found {number_of_words} total words")

    list_letters = get_dict_letters(book_text)

    for letter in list_letters[1:]:
        print(f"{letter['char']}: {letter['num']}")

main()
