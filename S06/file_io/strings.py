def is_palindrome(s):
    return s[::-1] == s
    # if len(s) in (0, 1):
    #     return True
    #
    # return (s[0] == s[-1]) and is_palindrome(s[1:-1])

# text = 'LMSSSMSMSMMSSSSLLSLSLS'
# cond = 'LSL' in text
#
#
# text.find('LSL', 0)

text = 'txt2 rotor'

# for length in range(2, len(text)+1):
for length in range(len(text), 2, -1):
    for start in range(len(text) - length + 1):
        substr = text[start:start+length]
        if is_palindrome(substr):
            print(substr)




