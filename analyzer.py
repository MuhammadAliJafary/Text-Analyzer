def char_count(s):
    """Count total characters recursively."""
    if s == "":
        return 0
    return 1 + char_count(s[1:])


def find_char(s, c):
    """Find index of character c in string s. Return -1 if not found."""
    
    def helper(index):
        if index == len(s):
            return -1
        if s[index] == c:
            return index
        return helper(index + 1)
    
    return helper(0)


def word_count(s):
    """Count words (split by spaces)."""
    s = s.strip()
    
    if s == "":
        return 0
    
    space = find_char(s, " ")
    
    if space == -1:
        return 1
    
    return 1 + word_count(s[space + 1:])


def clean_text(s):
    """Remove non-letters and make lowercase."""
    if s == "":
        return ""
    
    first = s[0].lower()
    rest = clean_text(s[1:])
    
    if first.isalpha() or first == " ":
        return first + rest
    
    return rest


def is_palindrome_phrase(s):
    """Check if phrase is palindrome (ignore spaces/punctuation)."""
    
    cleaned = clean_text(s).replace(" ", "")
    
    def helper(left, right):
        if left >= right:
            return True
        
        if cleaned[left] != cleaned[right]:
            return False
        
        return helper(left + 1, right - 1)
    
    return helper(0, len(cleaned) - 1)


def most_common(s):
    """Find most common letter."""
    
    cleaned = clean_text(s).replace(" ", "")
    
    if cleaned == "":
        return ""
    
    def count_in(text, c):
        if text == "":
            return 0
        return (1 if text[0] == c else 0) + count_in(text[1:], c)
    
    def best(text, current_best, best_count):
        if text == "":
            return current_best
        
        c = text[0]
        c_count = count_in(cleaned, c)
        
        if c_count > best_count:
            return best(text[1:], c, c_count)
        
        return best(text[1:], current_best, best_count)
    
    return best(cleaned, cleaned[0], 0)