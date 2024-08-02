import random
secret = random.randint(1,10)#生成一个随机数


temp = input("不妨猜一下小甲鱼心里想的一个数：")
guess = int(temp)
if guess == secret:
    print("恭喜你猜对了")
else:
    while guess!=secret:
        if guess>secret:
            print("大了，大了")
        else:
            print("小了，小了")
        temp=input("哎呀猜错了再猜一次吧：")
        guess = int(temp)
        if guess==secret:
            print("恭喜你猜对了\n"+"猜对了也没有奖励哦")
        else:
            if guess>secret:
                print("哥，大了，大了")
            else:
                print("嘿，小了，小了")
print("不玩了不玩了")
