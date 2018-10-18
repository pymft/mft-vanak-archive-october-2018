# f1(x:tuple) -> diff_values of tuple
# f1((1, 10)) -> 9
f1 = lambda x: x[1] - x[0]
# f2(s:str) -> reverted string
# f2('hello') -> 'olleh'
f2 = lambda s: s[::-1]

res = f2('hello')
print (res)
