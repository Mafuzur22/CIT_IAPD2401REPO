def is_palindrome(s):
  
    cleaned_str = ''.join(s.split()).lower()
    return cleaned_str == cleaned_str[::-1]


print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("Hello"))