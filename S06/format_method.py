# %s , %d %10.3f

#
# text = "welcome USER"
#
# text_new = text.replace('USER', 'John')
# print(text_new)

# print("welcome %s %s" % (first, last))
#

firstname, lastname = "John", "Smith"

text = "welcome {last}, {first} -------  {last} "
text_new = text.format(first=firstname, last=lastname)
print(text_new)


no_kw = "{} + {} = {}".format(1, 2, 3)
print(no_kw)


no_kw = "{0} , {1} , {2}".format(1, 2, 3)
print(no_kw)
no_kw = "{2} , {0} , {1}, {1}, {1}".format(1, 2, 3)   # args= (1, 2, 3)
print(no_kw)