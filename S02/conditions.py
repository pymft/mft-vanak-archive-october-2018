# cond1 = 10 >= 2
# cond2 = 0 > 100
# cond3 = 1 == 1
# cond4 = 1 != 1
#
# print(cond1)
# print(cond2)
# print(cond3)

num = 1100
cond1 = num > 10
cond2 = num < 1000
cond3 = cond1 and cond2
print(cond3)

#       <-cond1->    <-------->     <---------->
cond3 = num > 10 and num < 1000 and num % 2 == 0
print(cond3)


# True/false equivalents:
# numbers
0, 0.0, 0+0j  # False

cond5 = True or 0.0
print (cond5)

# str
cond6 = '' or True
print(cond6)

# list, tuple, dict
[], {}, ()  # False

set([])


