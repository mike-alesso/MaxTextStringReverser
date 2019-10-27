import argparse
import os
import re
import sys
""" 


"""


def filter_non_words(word):
    """
    Filtering words that have characters not found in a word

    Parameters:
    arg1 (str): Word to be checked

    Returns:
    bool: Returns true if only letters are present
    """

    regex = r'[\W0-9]'
    return not bool(re.search(regex, word, re.MULTILINE))


def find_largest_word(list_of_words):
    """
    Return the longest word and filter for non-words

    Parameters:
    arg1 (List(str)): List of words to be checked

    Returns:
    str or None: Largest word or None
    """
    result = list(filter(lambda w: filter_non_words(w), list_of_words))
    if result:
        return max(result, key=len)
    else:
        return


def read_file_to_list(filename):
    """
    Read a given file and split by lines to a set

    Parameters:
    arg1 (str): name of file to be parsed

    Returns:
    Set(str): set of lines from the file
    """
    with open(filename, 'r', encoding='utf8') as f:
        return set(f.read().splitlines())


def check_file(filename):
    """
    Check if a given file exists and can be opened

    Parameters:
    arg1 (str): name of file to be checked

    Returns:
    Bool: True or false depending on if file can be opened
    """
    if os.path.exists(filename) and os.access(filename, os.R_OK):
        return True
    else:
        print(f'File: {filename} does not exist or is not readable.')
        return False


def text_reverse(filename):
    """
    Attempts to find the largest word in a string and print it to the console

    Parameters:
    arg1 (str): name of file to be processed

    Returns:
    max_word: Largest word in file
    max_word_reversed: Largest word reversed
    None: returned if operation is not possible
    """
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
    """
    Parses commandline args

    Parameters:
    arg1 (str): name of file to be processed

    Returns:
    args: arguments object for arguments given at commandline
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Filename for the strings you want to provide", type=str)
    return parser.parse_args(args)


if __name__ == "__main__":
    main()

