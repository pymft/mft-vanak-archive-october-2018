a = 0
b = 1000

for i in range(100):
    m = (a+b)//2   # int((a+b)/2)
    ans = input("is it " + str(m) + " ?")
    if ans == 'H':
        a = m
    elif ans == 'L':
        b = m
    elif ans == 'Y':
        print('Hooray!')
        break