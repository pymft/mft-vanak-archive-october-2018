
def fun(*args):
    res = sum(args)
    return res

def my_range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]



args = (1, 2, 4, 7)

val = fun(1, 2, 2, 1, 100, 20)
print(val)