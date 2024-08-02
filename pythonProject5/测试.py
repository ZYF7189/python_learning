"""
给出三条线段
�
,
�
,
�
a,b,c 的长度，均是不大于
10000
10000 的正整数。打算把这三条线段拼成一个三角形，它可以是什么三角形呢？

如果三条线段不能组成一个三角形，输出Not triangle；
如果是直角三角形，输出Right triangle；
如果是锐角三角形，输出Acute triangle；
如果是钝角三角形，输出Obtuse triangle；
如果是等腰三角形，输出Isosceles triangle；
如果是等边三角形，输出Equilateral triangle。
如果这个三角形符合以上多个条件，请按以上顺序分别输出，并用换行符隔开。

输入格式
输入 3 个整数
�
a、
�
b 和
�
c。

输出格式
输出若干行判定字符串。

a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    print("Not triangle")
else:
    if a * a + b * b == c * c:
        print("Right triangle")
    elif a * a + b * b > c * c:
        print("Acute triangle")
    else:
        print("Obtuse triangle")

    if a == b or b == c:
        print("Isosceles triangle")
    if a == b == c:
        print("Equilateral triangle")
"""
"""
n = int(input())
local_time = 5 * n
luogu_time = 11 + 3 * n
if local_time < luogu_time:
    print('Local')
else:
    print('Luogu')
"""
"""
a, b, c = sorted(map(int, input().split()))
print(a, b, c)
"""

"""
def money_need(x, y):
    amount = float(n / x)
    if amount - int(amount) != 0:
        amount += 1
    return int(amount) * y


n = int((input()))
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


money1 = money_need(x1, y1)
money2 = money_need(x2, y2)
money3 = money_need(x3, y3)
print
print(min(money1, money2, money3))
"""

"""
maxtime = 8
mostunhappyday = 1
sch = []
for i in range(7):
    schooltime, extraltime = map(int, input().split())
    sch.append(schooltime + extraltime)
mosttime = sch[0]
judge = 0
for i in range(7):
    if sch[i] <= maxtime:
        continue
    else:
        if sch[i] > mosttime:
            mosttime = sch[i]
            judge = 1
            mostunhappyday = i + 1
if judge == 0:
    print('0')
else:
    print(mostunhappyday)

"""

"""
apples = [int(x) for x in input().split()]
height = int(input())
num = 0
for apple in apples:
    if apple <= height + 30:
        num += 1
print(num)
"""

"""
a, b, c = map(int, input().split())
a1 = max(a, b, c)
a2 = min(a, b, c)
print(f'{a2}/{a1}')
"""
"""
x, n = map(int, input().split())

distance = 250 * (n // 7) * 5  # 计算平日游泳距离
remainingDays = n % 7  # 计算剩余天数

if x + remainingDays - 1 >= 6:  # 判断是否需要减去周末休息日
    distance += 250 * (5 - max(0, x - 6))
else:
    distance += 250 * remainingDays

print(distance)
"""

"""
x = int(input())

if 0 <= x <=150:
    charge = float(x * 0.4463)

elif 151 <= x <= 400:
    charge = float(150 * 0.4463 + (x - 150) * 0.4663)
elif x >= 401:
    charge = float(150 * 0.4463 + (400 - 150) * 0.4663 + (x - 400) * 0.5663)
print("%.1f" % charge)
"""
"""
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year, month = map(int,input().split())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days[1] = 29
    print(days[month - 1])
else:
    print(days[month - 1])
"""

"""
str0 = input()
str1 = str0.replace('-', '')
str2 = str1[: 9 : 1]
str3 = str1[9:: 1]
num = 1
sum = 0
for element in str2:
    sum = sum + int(element) * num
    num += 1
mod_num = str(sum % 11)
if mod_num == 10:
    mod_num = 'X'
if mod_num == str3:
    print('Right')
else:
    true_str = str0[: 12: 1] + mod_num
    print(true_str)
"""

"""
num = int(input())
numbers = input().split() # 得到一个列表
min_num = int(numbers[0])
for i in range(num):
    if int(numbers[i]) < min_num:
        min_num = int(numbers[i])
print(min_num)
"""

"""
n, k = map(int, input().split())
A = []
B = []
for i in range(1, n+1):
    if i % k == 0:
        A.append(i)
    else:
        B.append(i)
len_A = len(A)
len_B = len(B)
count1 = 0
count2 = 0
for element in A:
    count1 += element
for element in B:
    count2 += element
average1 = float(count1 / len_A)
average2 = float(count2 / len_B)
print("%.1f %.1f" % (average1, average2))
"""

"""
a = int(input())
i = 2
while True:
    a = int(a / 2)
    if a == 1:
        break
    else:
        i += 1
print(i)
"""

"""数字三角形
n = int(input())
num = 1

for i in range(n, 0, -1):
    for j in range(i):
        print("{:02d}".format(num), end="")
        num += 1
    print()
"""

"""
n = int(input())
sum1 = 0
for i in range(1, n + 1):
    times = 1
    for k in range(1, i + 1):
        times *= k
    sum1 += times
print(sum1)
"""

"""
n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
min_score = min(scores)

summarize = sum(scores) - max_score - min_score
length = n - 2
average = summarize / length

print("%.2f" % average)
"""
"""
n, x = map(int, input().split())
count = 0
for num in range(1, n + 1):
    count += str(num).count(str(x))
print(count)
"""
"""
n = int(input())
numbers = input().split()
numbers = [int(num) for num in numbers]
compare = []
for count1 in range(n):
    flavor = 0
    for count2 in range(count1):
        if numbers[count2] < numbers[count1]:
            flavor += 1
    compare.append(flavor)
for num in compare:
    print(num, end=' ')

"""

"""
numbers = input().split()
numbers = [int(num) for num in numbers]
length = len(numbers)
del numbers[length - 1]
length -= 1
for i in range(length - 1, -1, -1):
    print(numbers[i], end=' ')
"""
"""
n = int(input())
list1 = []
while n != 1:
    list1.append(n)
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
list1.append(1)
list1 = list1[:: -1]
for i in list1:
    print(i, end=' ')
"""
"""
N = int(input())
scores = []
for _ in range(N):
    row = list(map(int, input().split()))
    scores.append(row)

count = 0
for i in range(N):
    for j in range(i+1, N):
        diff = [abs(scores[i][k] - scores[j][k]) for k in range(3)]
        if max(diff) <= 5 and sum(diff) <= 10:
            count += 1

print(count)
"""
"""
def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

# 测试
count = 0
for i in range(2333333, 23333334):
    result = []
    result = prime_factors(i)
    if len(result) == 12:
        count += 1
print(count)
"""
"""
from multiprocessing import Pool
from math import isqrt
from tqdm import tqdm


def prime_factors(n):
    factors = []
    # 利用试除法计算质因数
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def count_integers_with_prime_factors(start, end, num_factors):
    count = 0
    for i in range(start, end):
        if len(prime_factors(i)) == num_factors:
            count += 1
    return count


if __name__ == "__main__":
    start_num = 2333333
    end_num = 23333334
    num_factors = 12

    # 使用8个进程进行并行计算
    pool = Pool(processes=8)

    # 每个进程处理的整数范围
    chunk_size = (end_num - start_num) // 8
    ranges = [(start_num + i * chunk_size, start_num + (i + 1) * chunk_size) for i in range(8)]

    total_count = 0

    # 使用tqdm显示进度条
    with tqdm(total=end_num - start_num) as pbar:
        # 并行计算每个整数范围内满足条件的整数数量
        for result in pool.starmap(count_integers_with_prime_factors,
                                   [(start, end, num_factors) for start, end in ranges]):
            total_count += result
            pbar.update(chunk_size)

    # 总计数
    print("Total count:", total_count)
"""
"""
def source_diff(student1,student2):
    diff1 = abs(student1[0] - student2[0])
    diff2 = abs(student1[1] - student2[1])
    diff3 = abs(student1[2] - student2[2])
    total_diff = abs(sum(student1)-sum(student2))
    return total_diff <= 10 and diff3 <= 5 and diff2 <= 5 and diff1 <= 5


N = int(input())
students = []

for i in range(N):
    source = list(map(int,input().split()))
    students.append(source)


count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if source_diff(students[i], students[j]):
            count += 1
print(count)
"""
# L=0.130 s=0.000124 N=150 R1=0.8 R2=105000 C=0.000002
# H=N*X)/L*R1
# B=R2CY/NS

"""
numbers = []
while True:
    num_input = input()
    if num_input.lower() == "q":
        break
    try:
        num = float(num_input)
        numbers.append(num)
    except ValueError:
        print("错误请重试")
num_output = []
for i in numbers:
    i = float(i / 1000)
    H = float((105000 * i * 0.000002) / 0.0186)
    num_output.append(H)
print(len(num_output))
for i in num_output:
    print("%.2f" % i)
"""
"""
a = [0, 0, 0, 0, 0, 0, 0]


def check(win_numbers, tickets):
    count = 0
    for i in tickets:
        for j in win_numbers:
            if i == j:
                count += 1
    if count == 0:
        return
    else:
        a[count - 1] += 1


n = int(input())
win_numbers = list(map(int, input().split()))
for i in range(n + 1):
    tickets = list(map(int, input().split()))
    check(win_numbers, tickets)
for i in range(6, -1, -1):
    print(a[i], end=" ")
"""

import webbrowser
import pyautogui
import time
import winsound
import win32api

pyautogui.FAILSAFE = False


def fc_ssr(pic_name):
    try:
        pic = pyautogui.locateOnScreen(pic_name, confidence=0.7)
        xy = pyautogui.center(pic)
        pyautogui.click(xy)
        print(f'已识别到图像{pic_name}，继续执行')
    except:
        for i in range(0, 20):
            if i < 19:
                try:
                    time.sleep(1)
                    pic = pyautogui.locateOnScreen(pic_name, confidence=0.61)
                    xy = pyautogui.center(pic)
                    pyautogui.click(xy)
                    print(f'识别到并已单击目标{pic_name}(≧▽≦)')
                    break
                except:
                    print('没找到')
            else:
                print('没找到，已跳出循环')


def fc_a(pic_name):
    try:
        pic = pyautogui.locateOnScreen(pic_name, confidence=0.6)
        xy = pyautogui.center(pic)
        pyautogui.click(xy)
        print(f'已识别到图像{pic_name}，继续执行')
    except:
        for i in range(0, 20):
            if i < 19:
                try:
                    time.sleep(1)
                    pic = pyautogui.locateOnScreen(pic_name, confidence=0.6)
                    xy = pyautogui.center(pic)
                    pyautogui.click(xy)
                    print(f'识别到并已单击目标{pic_name}(≧▽≦)')
                    break
                except:
                    print('没找到')
            else:
                print('没找到，已跳出循环')


def fc(pic_name):  # 自定义单击函数
    try:
        pic = pyautogui.locateOnScreen(pic_name, confidence=0.7)
        xy = pyautogui.center(pic)
        pyautogui.click(xy)
        print(f'识别到并已单击目标{pic_name}(≧▽≦)')
    except:
        print('没找到目标(っ◞‸◟c)')
    return 0


record = 0
print('朋友你好。现在，我们来玩个游戏。赢了，我就放过你')
time.sleep(1)
print('输了，你就要迎接')
time.sleep(1)
print('严峻的！惩罚！！\nok，让我们开始吧')
time.sleep(1)
print('好，首先回答我\n小米公司的创始人是谁？')
for i in range(10):
    if i < 10:
        try:
            a = input("输入吧：")
            # global a
            if a == "雷军":
                print('好吧。你答对了')
                record = 1
                break
            else:
                print('很遗憾！回答错误！答案是雷军哦~')
                record = 0
                break
        except:
            time.sleep(1)
    else:
        print('wu')
print(f'哟西，这一轮已获得了{record}分')
time.sleep(1)
print('让我们继续吧')
time.sleep(0.5)
print('中国石油大学（华东）是哪一年建立的？')
for i in range(10):
    if i < 10:
        try:
            a = input("输入吧：")
            # global a
            if a == "1953":
                print('好吧。你答对了')
                record = record + 1
                break
            else:
                print('很遗憾！回答错误！是1953年成立的，你这人怎么一点学校情怀都没有啊')
                record = record + 0
                break
        except:
            time.sleep(1)
    else:
        print('wu')
print(f'哟西，这一轮已获得了{record}分')
time.sleep(1)
print('再来两题吧')
time.sleep(1)
print('中国石油大学（华东）现任校长是谁？')
for i in range(10):
    if i < 10:
        try:
            a = input("在这儿输入：")
            # global a
            if a == "郝芳":
                print('好吧。你答对了')
                record = record + 1
                break
            else:
                print('很遗憾！回答错误！是郝芳啦，你这人怎么一点学校情怀都没有啊（）')
                record = record + 0
                break
        except:
            time.sleep(1)
    else:
        print('wu')

print(f'现在你已获得了{record}分')
time.sleep(1)

print('最后一个问题\n2022年新高考Ⅰ卷数学22题\n已知函数f(x)=e^x - ax和g(x)=ax-lnx有共同最小值\n求a')
time.sleep(0.5)
print('给你10分钟思考一下')
for i in range(10):
    if i < 10:
        print(f'还剩{10 - i}分钟')
    else:
        print(' ')
print('10分钟到了')
c = int(input('请输入答案吧：'))
if c == 1:
    print('这都被你答出来了？ 你是战神吧')
    record = record + 1
else:
    print('这么简单都回答不出来？')

time.sleep(1)
print(f'你一共获得了{record}分')
if record >= 2:
    print('恭喜你正确回答数量超过半数。没有惩罚，奖励你玩原神吧！')
else:
    print('你的回答不堪入目，为了惩罚你，我要给你下载原神！')

time.sleep(3)
WM_APPCOMMAND = 0x319

APPCOMMAND_VOLUME_MAX = 0x0a
APPCOMMAND_VOLUME_MIN = 0x09

# 音量最大,播放原神启动音效
win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MAX * 0x10000)

# webbrowser.open('https://na-sycdn.kuwo.cn/1a0e9dd9445ec51d69105fbd6262d9dd/6565f86f/resource/n3/64/19/2452845354.mp3')

webbrowser.open('https://www.yuanshen.com/#/')  # 打开原神官网

fc_ssr('enter.png')
time.sleep(3)
fc_ssr('download.png')
time.sleep(0.5)

webbrowser.open('https://www.bilibili.com/video/BV1a14y1i7N4/')
time.sleep(3)
webbrowser.open('https://ys.mihoyo.com/')
time.sleep(0.5)
fc_ssr('yys.png')
time.sleep(3)
fc_ssr('mmdl.png')
time.sleep(0.5)
fc_ssr('number.png')
time.sleep(0.5)
pyautogui.typewrite('198637')
pyautogui.typewrite('21006')
time.sleep(0.2)
fc_a('keyword.png')
time.sleep(0.1)
pyautogui.typewrite('159951abcd')
fc_ssr('agree.png')
time.sleep(0.8)
fc_ssr('land.png')
# fc_ssr('jryx.png')
fc('never.png')
fc('men.png')
pyautogui.click()























