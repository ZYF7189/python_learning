"""if int(input('请输入您的身高')) <120:
    print("您可以免费")
elif int(input('请输入你的级别')) >3:
    print("您可以免费")
else:
    print("得加钱")
"""


# 判断语句的嵌套使用
"""if int(input("请输入你的身高：")) > 120:
    print("你的升高超过了120，不能免费")
    print('如果你的VIP级别超过3也可以免费')

    if int(input('请输入你的VIP级别：')) > 3:
        print('你可以免费游玩')
    else:
        print('你还是不可以免费')

else:
    print('你可以免费游玩')
"""

import random
num = random.randint(1,10)

if int(input('我已经想好了一个数，请猜一下：')) == num:
    print('恭喜你，猜对了')
elif int(input('再给你一次机会：')) == num:
    print('恭喜你，猜对了')
elif int(input('最后一次机会')) == num:
    print ('恭喜你，猜对了')
else:
    print("还是没有猜对")

