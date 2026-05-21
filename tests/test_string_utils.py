from string_utils import capitalize_words


def test_capitalize_words_multi_word():
    assert capitalize_words("hello world") == "Hello World"


def test_capitalize_words_empty_string():
    assert capitalize_words("") == ""
