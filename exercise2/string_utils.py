# Exercise 2: String Utilities
def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome, ignoring spaces and case.
    """
    cleaned_s = ''.join(s.lower().split())
    return cleaned_s == cleaned_s[::-1]

def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.
    """
    return s.title()

