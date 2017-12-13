import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')


test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'

#0 or more
test_patterns = ['sd*']
#1 or more
test_patterns = ['sd+']
#0 or 1
test_patterns = ['sd?']
#define specific
test_patterns = ['sd{3}']
test_patterns = ['sd{1,3}']
#followed by either s or d
test_patterns = ['s[sd]+']
#excludes
test_patterns = ['[^!.?]+']
#lower case chars
test_patterns = ['[a-z]+']
#upper case chars
test_patterns = ['[A-Z]+']
#special chars
test_patterns = [r'\d+']
d = #just digits
D = #non digits
s = #whiteSpace
S = #nonSpace
w = #alphanumeric
W = #nonAlphanumeric
multi_re_find(test_patterns, test_phrase)
