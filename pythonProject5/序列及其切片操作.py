# 列表，元组，字符串都是序列
# 切片指从主序列取出子序列
# [起始下标： 结束下标： 步长], 步长也可以是负数
# 对序列进行切片会产生新序列

# 进行切片，从1开始，倒4结束，步长为1
mylist = [0, 1, 2, 3, 4, 5, 6]
result1 = mylist[1: 4: 1]
print(result1)

# 从头开始，到尾部结束，步长是1
mytuple = (0, 1, 2, 3, 4, 5, 6)
result2 = mytuple[::]
print(result2)

# 从头开始到尾结束，步长为2
mystr = '01234567'
result3 = mystr[::2]
print(result3)
result4 = mystr[6:0:-1]  # 步长为-1时实现倒序
print(result4)

str = '万过月薪，员序程马黑来，nohtyp学'
"""
str_list = str.split('，')
new_str = str_list[1]
for i in range(5, -1):
    print(new_str[i:i-1:-1], end=' ')
"""
str1 = str[9: 4: -1]
print(str1)

str = input()
new_str = str[:: -1]
print(new_str)