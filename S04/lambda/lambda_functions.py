def f1(x):
    return x ** 2

f2 = lambda x: x ** 2

num = 10.1
print (f1(num))
print (f2(num))

# f(10)     <class 'int'>
# f(10.1)   <class 'float'>
# f         <class 'function'>