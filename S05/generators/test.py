import sys

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = sys.getsizeof(lst)
print(res)

lst = range(11)
res = sys.getsizeof(lst)
print(res)
