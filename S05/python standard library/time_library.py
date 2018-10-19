import time

t1 = time.time()
s = 0.0
for i in range(1000000):
    s += (i**2 /2.345345345)

t2 = time.time()
print(t2-t1)