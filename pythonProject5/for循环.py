#for 临时变量 in 待处理的数据集合（包括字符串，列表，元组）
#理论上来说for循环无法构建无限循环
"""
name = 'itheima is a brand of itcast'
count = 0
for i in name:
    if i == 'a':
        count += 1
print(f"{name}中有{count}个a")

#range语句，用于生成数字序列用于for循环
#range(num1,num2,step)获得一个从num1开始，到num2结束的数字序列，公差为step默认为1
#不含num2本身
for i in range(5,10,2):
    print(i, end=' ')
print()
for i in range(10):
    print(i)
#用range来控制for循环的次数

#小案例
end_num = int(input("请输入一个>=2的数字"))
oushu_num = 0
i = 0
for i in range (1,end_num):
    if i % 2 == 0:
        oushu_num += 1
print(f"从1到{end_num}之间的偶数有{oushu_num}个（不包括{end_num}）")
print(i)

get_str = '+'
print(" ", end=' ')
print(get_str)
print("",end=' ')
print(get_str+get_str+get_str)
print(get_str+get_str+get_str+get_str+get_str)

print("%3s" % get_str)
print("%2s" % get_str+get_str+get_str)
print("%s" % get_str*5)
"""
#综合案例,发工资
import random
salary = 10000
for i in range(1,21):
    num = random.randint(1,10)
    if num < 5:
        print(f"{i}号员工绩效为{num},不合格，不发工资")
        continue
    else:
        print(f"{i}号员工绩效为{num},发放工资1000元，账户余额还剩{salary-1000}元")
        salary -= 1000
        if salary < 1000:
            print("这个月工资发完了，大家下个月再领吧")
            break
