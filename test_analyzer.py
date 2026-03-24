from analyzer import (
    char_count, word_count, find_char,
    clean_text, is_palindrome_phrase,
    most_common
)

def test_char_count():
    assert char_count("hello") == 5
    assert char_count("") == 0
    assert char_count("a") == 1
    print("test_char_count: ALL PASSED")


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("one") == 1
    assert word_count("") == 0
    assert word_count(" spaces ") == 1
    print("test_word_count: ALL PASSED")


def test_find_char():
    assert find_char("hello", "e") == 1
    assert find_char("hello", "z") == -1
    assert find_char("hello", "h") == 0
    print("test_find_char: ALL PASSED")


def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("abc123") == "abc"
    assert clean_text("") == ""
    print("test_clean_text: ALL PASSED")


def test_is_palindrome_phrase():
    assert is_palindrome_phrase("racecar") == True
    assert is_palindrome_phrase("A man a plan a canal Panama") == True
    assert is_palindrome_phrase("hello") == False
    print("test_is_palindrome_phrase: ALL PASSED")


def test_most_common():
    assert most_common("aabbc") == "a"
    assert most_common("hello") == "l"
    print("test_most_common: ALL PASSED")


test_char_count()
test_word_count()
test_find_char()
test_clean_text()
test_is_palindrome_phrase()
test_most_common()

print("--- All tests passed! ---")