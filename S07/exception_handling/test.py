a = 1
b = 2
lst = [1, 2, 3]
try:
    res = a/b
    print(res)
    print(lst[1])
except IndexError:
    print("something went wrong with indices!")
except ZeroDivisionError:
    print("you were tryin' to divide sth to zero")
finally:
    print("FINALLY BLOCK")
print("After FINALLY BLOCK")