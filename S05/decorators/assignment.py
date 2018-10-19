# write decorator named `timeit`
import time


def timeit(f):
    def inner(*args, **kwargs):
        t1 = time.time()
        out = f(*args, **kwargs)
        t2 = time.time()
        print("elapsed time = ", t2-t1, "sec")
        return out
    return inner


@timeit
def zeta(s=2, n=100000):
    res = 0
    for i in range(1, n+1):
        res += 1 / (i ** s)
    return res


print(zeta())
# elapsed time = 0.123123412312 sec
