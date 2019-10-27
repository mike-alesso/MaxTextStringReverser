from MaxTextStringReverser import *


def test_find_largest_word():
    words = ["a", "ab", "abc", "abcd", "abcde"]
    assert find_largest_word(words) == "abcde"


def test_open_file(fs):
    """ Fake file content """
    file_content = """AbCdEfGhIj\nAbCfGhIj\nw\nwo\nwor\nword"""
    " Fake file "
    fs.create_file("/var/data/test1.txt")
    assert os.path.exists("/var/data/test1.txt")
    file = open("/var/data/test1.txt", "w")
    file.write(file_content)
    file.close()

    max_string, max_string_reversed = text_reverse("/var/data/test1.txt")
    assert max_string == "AbCdEfGhIj"
    assert max_string_reversed == "jIhGfEdCbA"


def test_open_file_doesnt_exist(fs):
    fs.create_file("/var/data/test1.txt")
    assert check_file("/var/data/nonexistent.txt") is False


def test_valid_string():
    """ Valid string """

    assert filter_non_words("Hello") is True
    assert filter_non_words("aAbBcCdDeE") is True


def test_invalid_string():
    """ Invalid string """

    assert filter_non_words(" 3!@#$%^&*(3 ") is False


def test_parser():
    args = parse_args(['testFilename'])
    assert args.filename is 'testFilename'
