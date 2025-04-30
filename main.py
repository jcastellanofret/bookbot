import sys
from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_dictionary

def get_book_text(file_path):
    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents 

def main(): 
    
    if len(sys.argv) != 2: 
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    # Retrieve all text content from the frankenstein.txt
    result = get_book_text(sys.argv[1])
    
    # This will count all words contained on frankenstein.txt
    num_words = get_num_words(result)

    # This will count characters
    char_dict = get_num_char(result)

    # This will sort dictionary and filter by alpha characters
    sorted_char_dict = get_sorted_dictionary(char_dict)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {len(num_words)} total words')
    print('--------- Character Count -------')
    
    for x, y in sorted_char_dict.items(): 
        print(f'{x}: {y}')

    print('============= END ===============')

main()