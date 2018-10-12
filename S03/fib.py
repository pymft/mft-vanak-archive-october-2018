# 20 th number of fibonacci series
a = 1
b = 1
# print(1, a)
# print(2, b)

for i in range(20):
    a, b = b, a+b
    # print(3+i, b)

# serendipitous
# serendipity

# print(20, b)


a = 1
b = 1
count = 2
# while b < 1e30:
while len(str(b)) < 30:
    a, b = b, a+b
    count += 1
print(count, b)

