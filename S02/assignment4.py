import random
secret = random.randint(0, 10)


for i in range(10):
    num = input('guess my secret number: ')
    num = int(num)
    if num > secret:
        print('my number is lesser than what said')
    elif num < secret:
        print('my number is greater than what said')
    else:
        print("BINGO")
        break