def check_char(char):
    char=char.lower()
    if char.isalpha() and len(char)==1:
        if char in 'aeiou':
            return "Vowel"
        else:
            return "Consonant"
print(check_char('a'))
print(check_char('b'))