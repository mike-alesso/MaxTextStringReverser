import argparse
import os
import re
import sys

"""
The Coding Challenge:

For this challenge, you can use node js, java, python, go, or whatever language you are most comfortable with,
to develop code that meets the challenge requirements listed below:

1. Read input from a file of words;
2. Find the largest word in the file
3. Transpose the letters in the largest word
4. Show the largest word and the largest word transposed
5. Demonstrate positive and negative test cases
6. Ensure you document code and instructions for building and running based on the response best practices above

Example Input File:
a
ab
abc
abcd
abcde

Output to console:
abcde
edcba
"""

""" 
    
TODO: Unit Tests 
    //Happy path simple
    Happy path huge input
    //File not found
    //Windows vs Linux new line
    //Numbers included
    //Non words
        //Symbols
        //Emoji
    //Chinese words
    //RTL language words like Hebrew and Arabic
    //Unicode Words - valid words
    //Unicode Chars - not words
TODO: Docstrings
TODO: Readme 
    Assumptions:
    - Each line has only 1 word
    - This will be initiated from the console
    - Words only contain language characters.
    - File is in UTF-8 encoding or parsable in UTF-8 (ASCII)
    How to run program
    How to run tests
TODO: Code Comments with O() notations for time and space"
"""


def filter_non_words(word):
    """
    Filtering words that have characters not found in a word

    Extended description of function.

    Parameters:
    arg1 (str): Word to be checked

    Returns:
    bool: Returns true if only letters are present

    """

    regex = r'[\W0-9]'
    return not bool(re.search(regex, word, re.MULTILINE))


def find_largest_word(list_of_words):
    result = list(filter(lambda w: filter_non_words(w), list_of_words))
    """"Return the maximum word by length"""
    if result:
        return max(result, key=len)
    else:
        return


def read_file_to_list(filename):
    """Open file"""
    with open(filename, 'r', encoding='utf8') as f:
        " Read file, split by lines, deduplicate using a set and return "
        return set(f.read().splitlines())


def check_file(filename):
    if os.path.exists(filename) and os.access(filename, os.R_OK):
        return True
    else:
        print(f'File: {filename} does not exist or is not readable.')
        return False


def text_reverse(filename):
    " Check that file is valid "
    if check_file(filename):
        " Read file and turn it into a list by line "
        list_of_words = read_file_to_list(filename)
        " Strip leading and trailing whitespace from the words in the list "
        list_of_words_stripped = map(str.strip, list_of_words)
        " Call function to retrieve largest word "
        max_word = find_largest_word(list_of_words_stripped)
        " Print word and word reversed (transposed) "
        if max_word:
            print(f'{max_word}')
            max_word_reversed = max_word[::-1]
            print(f'{max_word_reversed}')
            return max_word, max_word_reversed
        else:
            print('No valid words found in file.')
            return


def main():
    args = parse_args(sys.argv[1:])
    text_reverse(args.filename)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Filename for the strings you want to provide", type=str)
    return parser.parse_args(args)


if __name__ == "__main__":
    main()

