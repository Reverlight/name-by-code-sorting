"""This script gets names as input and output the dictionary with key of name
and value of first letter in name as a code.
The output is sorted by the code value or by the name key if the code is the same"""

import operator

def get_words_with_code(words):
    """Gets code of words using def get_code_of_word.
    Creates dictionary with value of code and key of word string
    """
    words_with_code = {}
    for word in words:
        code = get_code_of_word(word)
        words_with_code[word] = code
    return words_with_code


def get_code_of_word(word):
    """Gets code of word.
    By formula: first symbol of word - 'A' symbol code + 1"""
    first_word_symbol = word[0]
    code_first_symbol = ord(first_word_symbol)
    code_symbol_A = ord('A')
    code = code_first_symbol - code_symbol_A + 1
    return code

def capitalaze(words):
    """Creates a list of capitalazed words"""
    words_capitalazed = []
    for word in words:
        words_capitalazed.append(word.capitalize())
    return words_capitalazed


def main():
    """ Creates sorted dictionary with word code value and key value of word """
    words = ['andrey', 'max', 'sergei', 'alexey']
    #capitalazing every first symbol in the list
    words_capitalazed = capitalaze(words)
    #creating dictionary of words with thekey of word and the value of first symbol code in the word
    words_with_code = get_words_with_code(words_capitalazed)
    #sorting by value or by key if value is the same and getting dictionary
    words_with_code_sorted = sorted(words_with_code.items(), key=operator.itemgetter(1))
    words_with_code_sorted = dict(words_with_code_sorted)
    print(words_with_code_sorted)

if __name__ == '__main__':
    main()
    