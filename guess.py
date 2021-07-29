import random
start = input('決定隨機數字開始值: ')
end = input('決定隨機數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
    