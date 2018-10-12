a = 0
b = 1024
ans = ''

while ans != 'Y':
    m = (a+b)//2   # int((a+b)/2)
    ans = input("is it " + str(m) + " ?")
    if ans == 'H':
        a = m
    elif ans == 'L':
        b = m
