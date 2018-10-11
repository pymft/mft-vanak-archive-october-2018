# a-z A-Z _ 0-9
# int, float, str, bool, complex
a = 1
b = 1.2
text = "hello"
cond = True
z = 1 + 1j

# strings:
text2 = "hello there"
text3 = 'hello there'
long_text1 = "line1\nline2\nline3"
long_text = """line1
line2
line3"""

# list, tuple, set, dict
lst = [1, 2, 3, 4, 1.2, 'text', True]
lst[0]

# lists are mutable
lst[0] = 10000

# tuples:
# immutable: we cannot change 'em
tup = (1, 2, 3, 4, 1.2, 'text', True)
tup[1]
tup[1] = 10000   # WRONG!


# dict
# mutable
song = {'name': 'la vie en rose', 'singer': 'edith piaf'}
song['singer']
song['release'] = 1950


# set
set1 = {1, 2, 3, 4, 1, 1}
set2 = {1, 2, 3, 4}

1 in set1   # True
100 in set2   # False



print("Hello")
ta = type(a)
id(a)   # unique number, belongs to the object we're gonna check its address/id


# convert :
num = 1.2
num2 = int(num)
num3 = int("123")




# indices :
#      0  1  2  3  4  5  6  7  8
#           -7 -6 -5 -4 -3 -2 -1
lst = [2, 3, 4, 5, 6, 7, 8, 9, 0]
#           |<---lst2---->|
#           |x     x     x|  <---lst3

lst[7]
lst[-2]
lst2 = lst[2:7]
lst2 = lst[-7:-2]
lst2 = lst[2:-2]
lst[2:7:2]
# lst[6:1:-2]


# string --> immutable
#       0 2 4 6 8
text = "all work and no play makes Jack a dull boy!"
text[4:8]