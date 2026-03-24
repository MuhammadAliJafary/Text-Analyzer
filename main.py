from analyzer import (
    char_count, word_count, clean_text,
    is_palindrome_phrase, most_common
)

text = "A man a plan a canal Panama"

print("=== Recursive Text Analyzer ===")
print(f"Text: '{text}'")

print(f"Characters: {char_count(text)}")
print(f"Words: {word_count(text)}")
print(f"Cleaned: '{clean_text(text)}'")
print(f"Palindrome? {is_palindrome_phrase(text)}")
print(f"Most common letter: '{most_common(text)}'")