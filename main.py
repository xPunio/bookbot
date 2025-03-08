import sys
from stats import count_words, count_characters, prepare_display_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    args = sys.argv
    if len(args) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_contents = get_book_text(args[1])
    words_number = count_words(file_contents)
    char_dictionary = count_characters(file_contents)
    display_list = prepare_display_list(char_dictionary)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {words_number} total words')
    print('--------- Character Count -------')
    alpha = 'a'
    for element in display_list:
        check = alpha + element['char']
        if check.isalpha():
            print(f'{element['char']}: {element['num']}')
    print('============= END ===============')


main()
