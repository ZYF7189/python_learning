#布尔类型
result = 10 > 5
print(f"10>5的结果是{result},类型是{type(result)}")

#if和elif和else
"""
print("请输入你的年龄：")
age = int(input())
if age >= 18:
    print("已成年")
elif age>=5 and age <=17 :
    print("少年")
else :
    print("小孩")

key = input(print("小美是否喜欢我\n"))
if key == "yes" :
    print("明天就去表白")
    print("成功")
else:
    print("小丑")
"""

num = "10"
guess = input(print("我已经想好了一个数来猜猜看吧："))
if  guess == num:
    print("恭喜你猜对了")
else:
    print("猜错了再来一次吧")
    guess = input()
    if guess == num:
        print("这次终于猜对了")
    else:
        print("还有最后一次机会")
        guess = input()
        if guess == num:
            print('终于猜对了')
        else:
            print("你还是没有猜对我想的是%s" % num)
