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
TODO: Implementation
    //HappyPath
    Add Argparse for CLI
    Handle EOF, File not found and access denied 
    Ignore invalid words
    Handle no valid words
    
TODO: Unit Tests 
    Happy path simple
    Happy path huge input
    File not found
    Args not provided
    Numbers included
    Non words
        Symbols
        Emoji
        
    Chinese words
    RTL language words like Hebrew and Arabic
    Unicode Words - valid words
    Unicode Chars - not words
TODO: Docstrings
TODO: Readme 
    Assumptions:
    - Each line has only 1 word
    - This will be initiated from the console
    - 
    How to run program
    How to run tests
TODO: Code Comments with O() notations for time and space"
"""


def text_reverse():
    """TODO: Get console args for file name """
    " Get words from hardcoded filename and read to list "
    list_of_words = read_file_to_list('test.txt')
    " Call function to retrieve largest word "
    max_word = find_largest_word(list_of_words)
    " Print word and word reversed (transposed) "
    print(f'{max_word} {max_word[::-1]}')


def read_file_to_list(filename):
    """Open file"""
    with open(filename) as f:
        " Read file, split by lines, deduplicate using a set, return as a list"
        " TODO: filter non words "
        return list(set(f.read().splitlines()))


def find_largest_word(list_of_words):
    """Return the maximum word by length"""
    return max(list_of_words, key=len)


if __name__ == "__main__":
    text_reverse()
