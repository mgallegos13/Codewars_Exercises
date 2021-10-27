def is_palindrome(s):
    if s.lower() == s.lower()[::-1]:
        return True
    elif s.lower() != s.lower()[::-1]:
        return False
    else:
        return False
      
      
      
