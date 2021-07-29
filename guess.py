import random
r = random.randint(1, 100)
count = 0
while True:
    guess = input('猜一個數字: ')
    guess = int(guess)
    count += 1
    if guess == r:
        print('恭喜你答對了!')
        break
    elif guess > r:
        print('太大了!')
    elif guess < r:
        print('太小了!')
    print('你猜了', count, '次')
    