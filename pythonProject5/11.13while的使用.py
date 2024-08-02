i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
"""
一种写法
import random
num = random.randint(1,1)
n = int(input('我已经想好了一个数，快来猜一下：'))
flag = True
while n!=num:
    if n <num:
        print('小了')
    else:
        print('大了')
    n = int(input("猜错了再来一次吧"))
print('猜对了呢')
"""
import subprocess
subprocess.call(['python','11.7.py'])




