i = 1#基础循环
while i < 100:
    print("555")
    i = i + 1

#while循环里有了True和False
sum = 0
i = 1
while i <= 100 :
    sum += i
    i += 1
print("%d" % sum)

import random
num = random.randint(1,50)
amout = 1
flag = True
guess = int((input(print("来猜猜数吧"))))
if guess == num:
    print('猜对了')
else:
    while flag :
        guess = int((input("接着猜")))
        amout += 1
        if guess == num :
            flag = False
        elif guess > num :
            print("大了")
        elif guess < num :
            print("小了")

print("用了%d次猜对" % amout)