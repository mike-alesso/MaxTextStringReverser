from mtsr.mtsr import *


def test_find_largest_word():
    """ Find the longest word in a list """
    words = ["a", "ab", "abc", "abcd", "abcde"]
    assert find_largest_word(words) == "abcde"


def test_open_file_and_process_simple(fs):
    """ Fake file content simple content """
    file_content = """AbCdEfGhIj\nAbCfGhIj\nw\nwo\nwor\nword"""
    create_file(file_content, fs)
    max_string, max_string_reversed = text_reverse("/var/data/test1.txt")
    assert max_string == "AbCdEfGhIj"
    assert max_string_reversed == "jIhGfEdCbA"


def test_open_file_linux_newline(fs):
    """ Fake file content with linux newlines"""
    file_content = """AbCdEfGhIj\r\nAbCfGhIj\r\nw\r\nwo\r\nwor\r\nword"""
    create_file(file_content, fs)
    max_string, max_string_reversed = text_reverse("/var/data/test1.txt")
    assert max_string == "AbCdEfGhIj"
    assert max_string_reversed == "jIhGfEdCbA"


def test_open_file_complex(fs):
    """ Fake file content with complex words and non words """
    file_content = """4564642564\nAbCfGhIj\n/*/*/*!@#$%^&dfgdfgdg$%^$^$\nw\nwo\nwor\nword"""
    create_file(file_content, fs)
    max_string, max_string_reversed = text_reverse("/var/data/test1.txt")
    assert max_string == "AbCfGhIj"
    assert max_string_reversed == "jIhGfCbA"


def test_open_file_process_no_word(fs):
    """ Fake file content """
    file_content = """4564642564\nAbC5fGhIj\n/*/*/*!@#$%^&dfgdfgdg$%^$^$\n5w\nw6o\nwo8r\nw%ord"""
    create_file(file_content, fs)
    assert text_reverse("/var/data/test1.txt") is None


def test_open_file_and_reverse_unicode(fs):
    """ Fake file content """
    file_content = \
        "ぁあぃいぅうぇえぉおかがきぎ\n😃😃😃\nユーザー別サイト\n简体中文\n" \
        "크로스플랫폼으로\nמדוריםמבוקשיםأفضلالبحوث\nΣὲγνωρίζωἀπὸ\nДесятуюМеждународную\n" \
        "แผ่นดินฮั่นเสื่อมโทรมแสนสังเวช\n∮E⋅da=Q,n→∞,∑f(i)=∏g(i)\nfrançais\nmañana\n"
    create_file(file_content, fs)
    max_string, max_string_reversed = text_reverse("/var/data/test1.txt")
    assert max_string == "מדוריםמבוקשיםأفضلالبحوث"
    assert max_string_reversed == "ثوحبلالضفأםישקובמםירודמ"


def test_open_file_doesnt_exist(fs):
    """ Test opening a non existent file """
    fs.create_file("/var/data/test1.txt")
    assert check_file("/var/data/nonexistent.txt") is False


def test_valid_string():
    """ Valid string """

    assert filter_non_words("Hello") is True
    assert filter_non_words("aAbBcCdDeE") is True
    assert filter_non_words("ぁあぃいぅうぇえぉおかがきぎ") is True
    assert filter_non_words("ァアィイゥウェエォオカガキギ") is True
    assert filter_non_words("ABCDEFGHIJKLMNOPQRSTUVWXYZ") is True
    assert filter_non_words("abcdefghijklmnopqrstuvwxyz") is True
    assert filter_non_words("ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖÙÚÛÜÝÞ") is True
    assert filter_non_words("㐀㐁㐂㐃㐄㐅㐆㐇㐈㐉㐊㐋㐌㐍㐎㐏") is True


def test_invalid_string():
    """ Invalid string """

    assert filter_non_words(" 3!@#$%^&*(3 ") is False
    assert filter_non_words("ab3def") is False
    assert filter_non_words("     ") is False
    assert filter_non_words("😆😃") is False


def test_parser():
    """ Test argument parser """
    args = parse_args(['testFilename'])
    assert args.filename is 'testFilename'


def create_file(file_content, fs):
    """ Create fake file helper """
    fs.create_file("/var/data/test1.txt", encoding='utf8')
    assert os.path.exists("/var/data/test1.txt")
    file = open("/var/data/test1.txt", "w", encoding='utf8')
    file.write(file_content)
    file.close()
