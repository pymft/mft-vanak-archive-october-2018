num = 1000
upper = 9999
lower = 1000

if num <= upper and num >= lower:
    print('the number is in the range')
else:
    print('the number is out of range')


if num % 3 == 0:
    print('number is n = 3k')
else:
    if num % 3 == 1:
        print('number is n = 3k+1')
    else:
        print('number is n = 3k+2')

if num % 3 == 0:
    print('number is n = 3k')
elif num % 3 == 1:
    print('number is n = 3k+1')
else:
    print('number is n = 3k+2')